from  django.urls import path

from . import views


app_name = 'telegram'

urlpatterns = [
    path('marketing-message/<int:pk>/send/', views.MarketingMessageSendView.as_view(), name='marketing_meassage_send'),
    path('marketing-message/list/', views.MarketingMessageListView.as_view(), name='message_list'),
    path("message/create/", views.MarketingMessageCreateView.as_view(), name="message_create"),

    path("comment/", views.CommentProductListView.as_view(), name="comment_list"),
    path("comment/<int:pk>/update/", views.CommentProductUpdateView.as_view(), name="comment_update"),
]






