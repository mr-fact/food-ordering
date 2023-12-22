from rest_framework import serializers

from food.models import Food, Price, Category


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
        ]
