from rest_framework import serializers

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

    class Meta:
        model = Packet
        fields = [
            'id',
            'price',
            'user',
            'order',
            'number',
        ]
