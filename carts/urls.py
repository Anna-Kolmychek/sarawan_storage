from django.urls import path
from rest_framework import routers

from carts.apps import CartsConfig
from carts.views import CartItemViewSet, CartListAPIView, CartDestroyAPIView

app_name = CartsConfig.name

router = routers.DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('carts/', CartListAPIView.as_view(), name='cart'),
    path('carts/delete/', CartDestroyAPIView.as_view(), name='cart-delete'),
] + router.urls
