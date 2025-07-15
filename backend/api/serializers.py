
from rest_framework import serializers  

from product.models import Product, ProductMarketplaceUrl, Marketplace


class ProductMarketplaceSerializer(serializers.ModelSerializer):
    "Сериализатор модели ProductMarketplaceUrl"

    marketplace = serializers.CharField(source='marketplace_id.name', read_only=True)

    class Meta:
        model = ProductMarketplaceUrl
        fields = ("marketplace", "url")



class ProductSerializer(serializers.ModelSerializer):
    "Сериализотор модели Product"

    marketplaces = ProductMarketplaceSerializer(
        many=True,
        source="product_url",
        required=False,
        )

    class Meta:
        model = Product
        fields = ("id", "name", "description", "qrcode", "marketplaces")
        read_only_fields = ("id",)

    def validate_marketplace(self, values):
        for value in values:
            if not Marketplace.objects.filter(id=value).exists():
                raise serializers.ValidationError("Нет такого маркеплейса")
        return values

    def create(self, validated_data):
        marketplaces_data = validated_data.pop('marketplaces', [])
        print(marketplaces_data)