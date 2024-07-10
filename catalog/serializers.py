from rest_framework import serializers

from catalog.models import Category, Subcategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Категория
    """
    class Meta:
        model = Category
        fields = '__all__'
        # validators =


class SubcategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Подкатегория
    """
    class Meta:
        model = Subcategory
        fields = '__all__'
        # validators =


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Продукт
    """
    class Meta:
        model = Product
        fields = '__all__'
        # validators =
