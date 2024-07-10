from django.urls import include, path
from rest_framework.routers import DefaultRouter

from baskets.apps import BasketsConfig
from baskets.views import BasketProductModelViewSet, BasketViewSet

app_name = BasketsConfig.name

router = DefaultRouter()
router.register('carts', BasketViewSet, basename='carts')
router.register('carts/items', BasketProductModelViewSet, basename='carts-item')


urlpatterns = [
    path('', include(router.urls)),
]