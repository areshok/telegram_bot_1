from django.urls import path


from .views import (
    product_list, product_create, product_edit, marketplase_list,
    marketplace_create, marketplace_delete
)

app_name = 'product'

urlpatterns = [
    path('list/', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('edit/', product_edit, name='product_edit'),
    path('marketplace-list/', marketplase_list, name='marketplace_list'),
    path('marketplace-create/', marketplace_create, name='marketplace_create'),
    path('marketplace-delete/<id>/', marketplace_delete, name='marketplace_delete'),
]
