from rest_framework import viewsets, generics, status
from rest_framework import permissions
from rest_framework.response import Response

from carts.models import CartItem, Cart
from carts.serializers import CartItemSerializer, CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user).first()
        return CartItem.objects.filter(cart=cart).all()


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).all()


class CartDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=self.request.user).first()
        CartItem.objects.filter(cart=cart).all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
