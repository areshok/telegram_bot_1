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
        'detail/<pk>/',
        views.ProductDetail.as_view(),
        name='product_detail'
    ),
    path(
        'create/',
        views.ProductCreate.as_view(),
        name='product_create'
    ),
    path(
        'edit/<pk>/',
        views.ProductUpdate.as_view(),
        name='product_edit'
    ),
    path(
        'marketplace-list/',
        views.MarketplaceList.as_view(),
        name='marketplace_list'
    ),
    path(
        'marketplace-create/',
        views.MarketplaceCreate.as_view(),
        name='marketplace_create'
    ),
    path(
        'marketplace-delete/<pk>/',
        views.MarketplaceDelete.as_view(),
        name='marketplace_delete'
    ),
    path(
        '<int:pk>/qrcode-download/',
        views.QrcodeDowdnload.as_view(),
        name='qrcode_download'
    ),
]
