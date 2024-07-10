from django.urls import include, path
from rest_framework.routers import DefaultRouter

from baskets.apps import BasketsConfig
from baskets.views import BasketProductModelViewSet, BasketViewSet

app_name = BasketsConfig.name

router = DefaultRouter()
router.register('baskets', BasketViewSet, basename='baskets')
router.register('baskets/products', BasketProductModelViewSet, basename='baskets-products')


urlpatterns = [
    path('', include(router.urls)),
]