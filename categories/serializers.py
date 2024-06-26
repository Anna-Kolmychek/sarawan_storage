from rest_framework import serializers

from categories.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('pk', 'title', 'slug', 'preview')


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('pk', 'title', 'slug', 'preview', 'subcategories')
