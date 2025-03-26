from django.urls import path
from django.contrib.auth.views import LoginView

from .views import user_list, user_create, UserCreate

app_name = 'account'

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', UserCreate.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
]








