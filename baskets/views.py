from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from baskets.models import Basket, BasketProduct
from users.permissions import IsOwner
from .serializers import BasketTotalSerializer, BasketProductSerializer, BasketSerializer


class BasketViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketTotalSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        if self.request.user.is_authenticated:  # swagger
            return Basket.objects.filter(users=self.request.user).prefetch_related('products')


class BasketProductModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = BasketProduct.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:  # swagger
            return BasketProduct.objects.filter(cart__users=self.request.user).select_related('product')

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return BasketProductSerializer
        return BasketSerializer
