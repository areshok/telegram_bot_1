

from django.core.management.base import BaseCommand


from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Application, MessageHandler, filters, ContextTypes

from django.conf import settings

from tgm.models import  CommentProduct
from tgm.utils import create_or_update_user, create_product_comment, filter_marketplace, get_url_marketplace_product

class Command(BaseCommand):
    help = 'Запускает телеграм бота. Параметров нет'

    def handle(self, *args, **kwargs):
        print(settings.TOKEN_BOT)
        TelegramBot().run()



# t.me/ars_test_2_bot?start=id_tovara

class TelegramBot:
    def __init__(self):
        self.__BOT = Application.builder().token(token=settings.TOKEN_BOT).build()
        self.__marketplace_filter = filter_marketplace
        self.__marketplace_buttoms = filter_marketplace


    def run(self):
        ""
        self.__BOT.add_handler(CommandHandler('start', self.start_get_id_product))
        # оценка
        self.__BOT.add_handler(
            MessageHandler(
                filters.Regex('Ozon|яндекс'), self.get_marketplace)
        )
        # отзыв
        self.__BOT.add_handler(
            MessageHandler(
                filters.Regex('1|2|3|4|5'), self.get_score)
        )
        # оценить товар на маркетплейсе

        self.__BOT.add_handler(
            MessageHandler(
                filters.Regex('.*'), self.get_comment_product)
            )
        self.__BOT.run_polling()

    async def start_get_id_product(self, update, context):
        ""
        user = update.effective_user
        print(user)
        try:
            id_tovara = (update.message.text.split())[1]
        except IndexError:
            id_tovara = None
            await update.message.reply_text(
                text='Нет товара',
                reply_markup=ReplyKeyboardRemove()
            )

        # добавляем id товара
        context.user_data['messages'] = {'id_tovara': id_tovara}
        context.user_data['messages']['t_user'] = user.id
        print(context.user_data['messages'])

        await create_or_update_user(user)
        # отправка кнопок маркетплейсов
        button = ReplyKeyboardMarkup([['яндекс', 'Ozon']])
        await update.message.reply_text(
            text='Где вы купили товар',
            reply_markup=button
        )

    async def get_marketplace(self, update, context):
        ""
        #print(update.message.text)
        # добавляем маркетплейс
        context.user_data['messages']['marketplace'] = update.message.text
        #print(context.user_data['messages'])
        button = ReplyKeyboardMarkup([['1',], ['2',], ['3',], ['4',], ['5',]])
        await update.message.reply_text(
            text='score',
            reply_markup=button
        )

    async def get_score(self, update, context):
        ""
        score = update.message.text
        context.user_data['messages']['score'] = score
        print(context.user_data['messages'])
        if int(score) <= 3:
            await update.message.reply_text(
                text='Напишите отзыв',
                reply_markup=ReplyKeyboardRemove(),
            )
        else:
            await create_product_comment(context.user_data['messages'])
            # добавить ссылку на маркептлейс
            url = get_url_marketplace_product(
                context.user_data['messages']['product_id'],
                context.user_data['messages']['marketplace']
            )
            await update.message.reply_text(
                text=f'Оставьте отзыв на маркетплейсе \n {url}',
                reply_markup=ReplyKeyboardRemove()
            )

    async def get_comment_product(self, update, context):
        ""
        comment = update.message.text
        context.user_data['messages']['comment'] = comment
        print(context.user_data['messages'])
        await create_product_comment(context.user_data['messages'])
        await update.message.reply_text('Отзыв принят')
