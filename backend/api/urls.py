

from django.urls import path, include
from rest_framework import routers 

from .views import ProductViewSet

api_router = routers.DefaultRouter()
api_router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(api_router.urls))

]
