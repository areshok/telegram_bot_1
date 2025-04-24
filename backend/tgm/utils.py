from asgiref.sync import sync_to_async


from tgm.models import TelegramProfile, CommentProduct
from product.models import Marketplace, Product

@sync_to_async
def create_or_update_user(user):
    "Проверяет и создает запись пользователя телеграм"
    exists = TelegramProfile.objects.filter(extend_id=user.id).exists()
    if exists and user.is_bot == False:
        t_user = TelegramProfile.objects.get(extend_id=user.id)
        t_user.username = user.username
        t_user.first_name = user.first_name
        t_user.last_name = user.last_name
        t_user.save()
    else:
        TelegramProfile.objects.create(
            extend_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )

@sync_to_async
def create_product_comment(comment):
    if comment.get('id_tovara') is not None:
        t_user = TelegramProfile.objects.get(extend_id=comment.get('t_user'))
        product = Product.objects.get(id=int(comment.get('id_tovara')))
        CommentProduct.objects.create(
            product_id=product,
            telegram_profile_id=t_user,
            comment=comment.get('comment'),
            score=comment.get('score'),
        )


def filter_marketplace():
    "Создает фильтр маркетплейсов для telegram bot'а"
    marketplaces = []
    for market in Marketplace.objects.all():
        marketplaces.append(market)
    return '|'.join(marketplaces)
