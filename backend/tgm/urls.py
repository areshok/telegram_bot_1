from  django.urls import path

from . import views


app_name = 'telegram'

urlpatterns = [
    path('marketing-message/<int:pk>/send/', views.MarketingMessageSendView.as_view(), name='marketing_meassage_send'),
    path('marketing-message/list/', views.MarketingMessageListView.as_view(), name='marketing_message_list'),
]






