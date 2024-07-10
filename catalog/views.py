from rest_framework import generics
from rest_framework.permissions import AllowAny

from catalog.models import Category, Subcategory, Product
from catalog.paginations import CatalogPagination
from catalog.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    """
    Создание Категории
    """
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryUpdateAPIView(generics.UpdateAPIView):
    """
    Редактирование Категории
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class CategoryDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление Категории
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class CategoryListAPIView(generics.ListAPIView):
    """
    Список Категорий
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CatalogPagination


class SubcategoryCreateAPIView(generics.CreateAPIView):
    """
    Создание Подкатегории
    """
    serializer_class = SubcategorySerializer
    permission_classes = [AllowAny]


class SubcategoryUpdateAPIView(generics.UpdateAPIView):
    """
    Редактирование Подкатегории
    """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    permission_classes = [AllowAny]


class SubcategoryDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление Подкатегории
    """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    permission_classes = [AllowAny]


class SubcategoryListAPIView(generics.ListAPIView):
    """
    Список Подкатегорий
    """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CatalogPagination


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Создание Продукта
    """
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    Редактирование Продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление Продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]


class ProductListAPIView(generics.ListAPIView):
    """
    Список Продуктов
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CatalogPagination
