
from django.core.management.base import BaseCommand

import telegram
from telegram import Update
from telegram.ext import Application

from django.conf import settings

from tgm.models import TelegramProfile, CommentProduct

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **kwargs):
        start_bot()


def start_bot():
    #bot = Application.builder().token(os.getenv('T_BOT_TOKEN'))
    print(settings.T_BOT_TOKEN)

