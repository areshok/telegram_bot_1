from django.db.models.query import QuerySet
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import response

import asyncio
from asgiref.sync import sync_to_async
# Create your views here.
from telegram.ext import Application
from telegram import Bot

from .models import TelegramProfile, MarketingMessage, CommentProduct
from .forms import CommentProductFormUser, MarketingMessageForm

class MarketingMessageSendView(LoginRequiredMixin, View):
    "Рассылка маркетингового сообщения"

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(MarketingMessage, id=kwargs.get('pk'))
        t_users = TelegramProfile.objects.all()
        text = f'{message.title}\n{message.body}'
        # отработка бота
        bot = Bot(token=settings.TOKEN_BOT)
        for t_user in t_users:
            if message.image:
                try:
                    asyncio.run(bot.send_photo(
                        chat_id=t_user.extend_id,
                        photo=open(message.image.path, "rb"),
                        caption=text)
                        )
                    message.status = MarketingMessage.Status.OK
                except Exception:
                    message.status = MarketingMessage.Status.ER
            else:
                try:
                    asyncio.run(bot.send_message(
                        chat_id=t_user.extend_id,
                        text=text)
                        )
                    message.status = MarketingMessage.Status.OK
                except Exception:
                    message.status = MarketingMessage.Status.ER
        bot.close()
        message.save()
        return redirect(reverse('telegram:message_list'))

class MarketingMessageListView(ListView):
    "Список рекламных сообщений"
    model = MarketingMessage
    template_name = 'telegram/marketing_message_list.html'
    paginate_by = settings.PAGINATE_COUNT


class MarketingMessageDetailView(DetailView):
    "Просмотр рекламного сообщения"
    model = MarketingMessage
    template_name = 'telegram/marketing_message_detail.html'


class MarketingMessageCreateView(CreateView):
    "Создать рекламное сообщение"
    model = MarketingMessage
    form_class = MarketingMessageForm
    template_name = 'telegram/marketing_message_create.html'
    success_url = reverse_lazy("telegram:message_list")


class MarketingMessageUpdateView(UpdateView):
    "Изменение рекламного сообщения"
    model = MarketingMessage
    template_name = 'telegram/marketing_message_create.html'


class MarketingMessageDeleteView(DeleteView):
    "Удаление рекламного сообщения"
    pass


class CommentProductListView(ListView):
    ""
    model = CommentProduct
    template_name = 'telegram/comment_product_list.html'
    context_object_name = 'page_obj'

    def get_queryset(self):
        return CommentProduct.notviewed.filter(score__lte=3)


class CommentProductUpdateView(UpdateView):
    "Обновление информации комментария для пользователя"
    model = CommentProduct
    form_class = CommentProductFormUser
    template_name = 'telegram/comment_product_detail.html'
    success_url = reverse_lazy("telegram:comment_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.cleaned_data.get('status_boolean'):
            self.object.status = CommentProduct.Status.VIEWED
            self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)
    
