# food/serializers.py

from rest_framework import serializers

from account.models import Order
from food.models import Food, Price, Category, Packet


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


class FoodSerializer(serializers.ModelSerializer):
    """
    Serializer for the Food model.
    """
    category = CategorySerializer()

    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'description',
            'category',
        ]


class PriceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Price model.
    """
    food = FoodSerializer()

    class Meta:
        model = Price
        fields = [
            'id',
            'food',
            'short_title',
            'title',
            'description',
            'price',
            'status',
        ]


class PacketSerializer(serializers.ModelSerializer):
    """
    Serializer for the Packet model.
    """
    price = PriceSerializer(read_only=True)

    class Meta:
        model = Packet
        fields = [
            'id',
            'price',
            'user',
            'order',
            'number',
        ]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    packets = PacketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'paid',
            'packets',
        ]

    def create(self, validated_data):
        """
        Custom create method to handle Order creation with the user from the request context.
        """
        return Order.objects.create(self.context.get('request').user)
