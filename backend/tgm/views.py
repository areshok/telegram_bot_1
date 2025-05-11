from django.shortcuts import render

from django.urls import reverse
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


class MarketingMessageSendView(LoginRequiredMixin, View):
    "Рассылка маркетингового сообщения"

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(MarketingMessage, id=kwargs.get('pk'))
        t_users = TelegramProfile.objects.all()
        # отработка бота
        bot = Bot(token=settings.T_BOT_TOKEN)
        for t_user in t_users:
            try:
                asyncio.run(bot.send_message(chat_id=t_user.extend_id, text='test'))
                message.Status.OK
            except Exception:
                message.Status.ER
        bot.close()
        message.save()
        return redirect(reverse('telegram:marketing_message_list'))

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
    template_name = 'telegram/marketing_message_create.html'


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


class CommentProductUpdateView(UpdateView):
    ""
    model = CommentProduct
    template_name = 'telegram/comment_product_update.html'
