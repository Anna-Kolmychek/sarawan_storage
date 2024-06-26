from rest_framework import serializers

from carts.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def to_internal_value(self, data):
        user = self.context['request'].user
        cart = Cart.objects.filter(user=user)
        if cart:
            cart = cart[0]
        else:
            cart = Cart.objects.create(user=user)
        data['cart'] = cart.pk
        return super().to_internal_value(data)


    def create(self, validated_data):
        # user = self.context['request'].user
        cart = validated_data['cart']
        product = validated_data['product']
        quantity = validated_data['quantity']

        cart_item = CartItem.objects.filter(cart=cart, product=product)

        if cart_item:
            cart_item = cart_item[0]
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item = super().create(validated_data)

        return cart_item


class CartItemShortSerializer(serializers.ModelSerializer):
    product_pk = serializers.IntegerField(source='pk')
    product_title = serializers.CharField(source='product.title')

    class Meta:
        model = CartItem
        fields = ('product_pk', 'product_title', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemShortSerializer(source='cartitem_set', many=True, read_only=True)
    total_sum = serializers.SerializerMethodField(read_only=True)
    total_quantity = serializers.SerializerMethodField(read_only=True)

    def get_total_sum(self, obj):
        total_sum = 0
        for cart_item in obj.cartitem_set.all():
            total_sum += cart_item.quantity * cart_item.product.price
        return total_sum

    def get_total_quantity(self, obj):
        total_quantity = 0
        for cart_item in obj.cartitem_set.all():
            total_quantity += cart_item.quantity
        return total_quantity

    class Meta:
        model = Cart
        fields = ('cart_items', 'total_sum', 'total_quantity')


