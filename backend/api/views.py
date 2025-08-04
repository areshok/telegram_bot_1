from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer, ProductCreateSerialize

from rest_framework import viewsets

from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerialize
        return ProductSerializer
