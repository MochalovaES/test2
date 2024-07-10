
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from baskets.models import Basket, BasketProduct
from catalog.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_id = serializers.CharField(source='product.id')

    class Meta:
        model = BasketProduct
        fields = ('id', 'product', 'product_id', 'quantity', 'price', 'total_price')


class BasketTotalSerializer(serializers.ModelSerializer):
    products = BasketSerializer(source='basket_products', many=True, read_only=True)
    total_cost = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'products', 'total_cost',)

    @staticmethod
    def get_total_cost(obj):
        return obj.total_cost()


class BasketProductSerializer(serializers.ModelSerializer):
    total_price = SerializerMethodField()

    class Meta:
        model = BasketProduct
        fields = ('id', 'product', 'quantity', 'price', 'total_price',)
        read_only_fields = ('baskets', 'price',)

    def create(self, validated_data):
        request = self.context.get('request')
        product = validated_data['product']
        try:
            basket = Basket.objects.get(
                users=request.user,
                order=None
            )
        except Basket.DoesNotExist:
            basket = Basket.objects.create(
                users=request.user
            )
        basket_product, _ = BasketProduct.objects.update_or_create(
            basket=basket,
            product=product,
            defaults={
                'quantity': validated_data['quantity'],
                'price': product.price
            },
        )
        return basket_product

    def update(self, instance, validated_data):
        instance.price = instance.product.price
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance

    @staticmethod
    def get_total_price(obj):
        return obj.total_price()
