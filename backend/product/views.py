import os
from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View

from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Product, Marketplace, ProductMarketplaceUrl
from .forms import ProductFormCreate, MarketplaceFormCreate, ProductFormUpdate, ProductMarketplaceForm
from account.mixins import AdminRequriedMixin
from account.models import User

from django.http import HttpResponseRedirect


# Товары
class ProductDetail(LoginRequiredMixin, DetailView):
    "Просмотр товара"
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marketplaces'] = ProductMarketplaceUrl.objects.filter(
            product_id=self.object
        )
        return context


class ProductList(LoginRequiredMixin, ListView):
    "Список товаров"
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 10


class ProductCreate(LoginRequiredMixin, CreateView):
    "Создание товара"

    model = Product
    form_class = ProductFormCreate
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product:product_list')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    "Редактирование товара"

    model = Product
    form_class = ProductFormUpdate
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse_lazy('product:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = self.get_formset(self.request.POST, instance=self.object)
        else:
            context['formset'] = self.get_formset(instance=self.object)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = self.get_formset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)
        return response

    def get_formset(self, data=None, instance=None):
        available_marketplaces = self.get_available_marketplaces(instance)
        ProductMarketplaceFormSet = inlineformset_factory(
            Product,
            ProductMarketplaceUrl,
            form=ProductMarketplaceForm,
            extra=len(available_marketplaces),
            can_delete=True
        )
        return ProductMarketplaceFormSet(
            data,
            instance=instance,
            form_kwargs={
                'available_marketplaces': available_marketplaces
            }
        )

    def get_available_marketplaces(self, product):
        existing_marketplaces = ProductMarketplaceUrl.objects.filter(
            product_id=product
            ).values_list('marketplace_id', flat=True)
        return Marketplace.objects.exclude(id__in=existing_marketplaces)


class ProductDelete(View):
    "Удаление товара"

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



# Qrcode
class QrcodeDowdnload(LoginRequiredMixin, View):
    "Скачать Qrcode"

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)

        if not product.qrcode or not os.path.isfile(product.qrcode.path):
            raise Http404('нет файла')

        with open(product.qrcode.path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')
            response['Content-Disposition'] = (
                f'attachment; '
                f'filename="{os.path.basename(product.qrcode.name)}"'
            )
            return response


class QrcodeCreate(LoginRequiredMixin, View):
    "Создать Qrcod"
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)

        # тут создание qrcod

        return redirect(reverse_lazy("product:product_detail", kwargs={'pk': product.id}))



class QrcodeDelete(LoginRequiredMixin, View):
    "Удалить Qrcode"
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        product.qrcode.delete()
        product.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# Маркетплейсы
class MarketplaceList(AdminRequriedMixin, ListView):
    "Список маркетплейсов"

    model = Marketplace
    template_name = 'product/marketplace_list.html'
    context_object_name = 'marketplaces'


class MarketplaceCreate(AdminRequriedMixin, CreateView):
    "Создание маркетплейса"

    model = Marketplace
    form_class = MarketplaceFormCreate
    template_name = 'product/marketplace_create.html'
    success_url = reverse_lazy('product:marketplace_list')


class MarketplaceDelete(AdminRequriedMixin, DeleteView):
    "Удаление маркеплейса"

    model = Marketplace
    success_url = reverse_lazy('product:marketplace_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
