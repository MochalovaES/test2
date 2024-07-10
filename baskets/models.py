from django.db import models
from django.utils import timezone

from catalog.models import Product
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Basket(models.Model):
    """
    Создание модели Корзина
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, related_name='basket', through='BasketProduct')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def total_cost(self):
        return sum([basket_products_row.total_price() for basket_products_row in BasketProduct.objects.filter(basket=self)])

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketProduct(models.Model):
    """
    Создание модели Корзина- Продукт
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='Корзина')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def total_price(self):
        return int(self.quantity) * int(self.price)

    def __str__(self):
        return f'{self.product}- {self.quantity}'

    class Meta:
        verbose_name = 'Корзина- Продукт'
        verbose_name_plural = 'Корзина- Продукты'

