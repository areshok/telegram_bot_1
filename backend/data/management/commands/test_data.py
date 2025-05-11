from django.core.management.base import BaseCommand


from product.models import Product, Marketplace, ProductMarketplaceUrl
from tgm.models import CommentProduct, MarketingMessage


class Command(BaseCommand):
    help = 'Запускает телеграм бота. Параметров нет'

    def handle(self, *args, **kwargs):
        create_test_products()
        create_test_marketplaces()
        create_test_productmarketplaces()


def create_test_products():
    "Тестовые данные модели Product"
    print('Создание тостовых товаров')
    for i in range(1, 20):
        Product.objects.create(
            name=f'Имя товара {i}',
            description=f'Описание товара {i}'
        )


def create_test_marketplaces():
    "Тестовые данные модели Marketplace"
    print('Создание тестовых маркетплейсов')
    marketplaces = ['yandex', 'ozon', 'wildberries']
    for name in marketplaces:
        Marketplace.objects.create(name=name)


def create_test_productmarketplaces():
    "Тестовые данные для модели ProductMarketplace"
    print('Создание тестовых url для товаров')
    marketplaces = Marketplace.objects.all()
    products = Product.objects.all()
    for product in products:
        for marketplace in marketplaces:
            ProductMarketplaceUrl.objects.create(
                product_id=product,
                marketplace_id=marketplace,
                url=f'https://{marketplace.name}.ru/{product.name}'
            )

def create_test_marketingmessage():
    pass


def create_test_commentproduct():
    pass


