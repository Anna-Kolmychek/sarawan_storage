from django.db import models

from products.models import Product
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='пользователь')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False, verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')
