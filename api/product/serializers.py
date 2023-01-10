from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'category', 'brand', 'tag', 'color', 'size', 'thumbnail', 'price', 'is_offer',
                  'offer_price', 'short_description', 'long_description')
