from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.CharField(source='subcategory_title', read_only=True)
    category = serializers.CharField(source='category_title', read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'title', 'slug', 'image1', 'image2', 'image3', 'price', 'subcategory', 'category']
