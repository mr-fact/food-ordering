from rest_framework import serializers

from account.models import Order
from food.models import Food, Price, Category, Packet


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


class FoodSerializer(serializers.ModelSerializer):
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
        return Order.objects.create(self.context.get('request').user)
