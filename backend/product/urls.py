from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('',
         views.ProductList.as_view(),
         name='product_list'),
    path('<int:pk>/detail/',
         views.ProductDetail.as_view(),
         name='product_detail'),
    path('create/',
         views.ProductCreate.as_view(),
         name='product_create'),
    path('<int:pk>/update/',
         views.ProductUpdate.as_view(),
         name='product_update'),
    path('<int:pk>/delete/',
         views.ProductDelete.as_view(),
         name='product_delete'),

    path('marketplaces/',
         views.MarketplaceList.as_view(),
         name='marketplace_list'),
    path('marketplace/create/',
         views.MarketplaceCreate.as_view(),
         name='marketplace_create'),
    path('marketplace/<pk>/delete/',
         views.MarketplaceDelete.as_view(),
         name='marketplace_delete'),

    path('<int:pk>/qrcode-download/',
         views.QrcodeDowdnload.as_view(),
         name='qrcode_download'),
    path('<int:pk>/qrcode-create/',
         views.QrcodeCreate.as_view(),
         name='qrcode_create'),
    path('<int:pk>/qrcode-delete/',
         views.QrcodeDelete.as_view(),
         name='qrcode_delete'),
]
