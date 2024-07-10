from catalog.apps import CatalogConfig

from django.urls import path

from catalog.views import CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView, \
    SubcategoryCreateAPIView, SubcategoryUpdateAPIView, SubcategoryDestroyAPIView, CategoryListAPIView, \
    SubcategoryListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductListAPIView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/category/', CategoryCreateAPIView.as_view(), name='create_category'),  # Создание категории
    path('update/category/<int:pk>/', CategoryUpdateAPIView.as_view(), name='update_category'), # Редактирование категории
    path('destroy/category/<int:pk>/', CategoryDestroyAPIView.as_view(), name='destroy_category'),  # Удаление категории
    path('list/category/', CategoryListAPIView.as_view(), name='list_category'),  # Список категорий
    path('create/subcategory/', SubcategoryCreateAPIView.as_view(), name='create_subcategory'),  # Создание подкатегории
    path('update/subcategory/<int:pk>/', SubcategoryUpdateAPIView.as_view(), name='update_subcategory'), # Редактирование подкатегории
    path('destroy/subcategory/<int:pk>/', SubcategoryDestroyAPIView.as_view(), name='destroy_subcategory'), # Удаление подкатегории
    path('list/subcategory/', SubcategoryListAPIView.as_view(), name='list_subcategory'),  # Список подкатегорий
    path('create/product/', ProductCreateAPIView.as_view(), name='create_product'),  # Создание продукта
    path('update/product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),  # Редактирование продукта
    path('destroy/product/<int:pk>/', ProductDestroyAPIView.as_view(), name='destroy_product'),  # Удаление продукта
    path('list/product/', ProductListAPIView.as_view(), name='list_product'),  # Список продуктов
]
