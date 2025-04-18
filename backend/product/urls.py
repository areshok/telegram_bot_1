from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path(
        '',
        views.ProductList.as_view(),
        name='product_list'
    ),
    path(
        '<int:pk>/detail/',
        views.ProductDetail.as_view(),
        name='product_detail'
    ),
    path(
        'create/',
        views.ProductCreate.as_view(),
        name='product_create'
    ),
    path(
        '<int:pk>/update/',
        views.ProductUpdate.as_view(),
        name='product_update'
    ),

    path(
        'marketplaces/',
        views.MarketplaceList.as_view(),
        name='marketplace_list'
    ),
    path(
        'marketplace/create/',
        views.MarketplaceCreate.as_view(),
        name='marketplace_create'
    ),
    path(
        'marketplace/<pk>/delete/',
        views.MarketplaceDelete.as_view(),
        name='marketplace_delete'
    ),

    path(
        '<int:pk>/qrcode-download/',
        views.QrcodeDowdnload.as_view(),
        name='qrcode_download'
    ),
]
