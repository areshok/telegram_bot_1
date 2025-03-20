from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Product, Marketplace
from .forms import ProductFormCreate, MarketplaceCreateForm

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductFormCreate(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductFormCreate()
        return render(request, 'product/product_create.html', {'form': form})

def product_edit(request):
    return render(request, 'product/product_edit.html')

def marketplase_list(request):
    marketplaces = Marketplace.objects.all()
    context = {'marketplaces': marketplaces}
    return render(request, 'product/marketplace_list.html', context)


def marketplace_create(request):
    if request.method == 'POST':
        form = MarketplaceCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('product:marketplace_list')
    else:
        form = MarketplaceCreateForm()
        context = {'form': form}
        return render(request, 'product/merketplace_create.html', context)


def marketplace_delete(request, id):
    marketplace = get_object_or_404(Marketplace, id=id)
    marketplace.delete()
    return redirect('product:marketplace_list')

