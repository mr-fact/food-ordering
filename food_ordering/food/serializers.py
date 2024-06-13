# food/serializers.py

from rest_framework import serializers

from account.models import Order, User
from food.models import Food, Price, Category, Packet, Rating


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


class InnerUserSerializer(serializers.CharField):
    def to_representation(self, phone):
        return f'{phone[:4]}****{phone[-3:]}'


class RatingSerializer(serializers.ModelSerializer):
    user = InnerUserSerializer(read_only=True, source='user.phone')
    # price = PriceSerializer(read_only=True)

    class Meta:
        model = Rating
        # depth = 1
        fields = [
            'user',
            'price',
            'created_at',
            'grade',
            'comment',
        ]
        extra_kwargs = {
            'created_at': {'read_only': True, },
            'comment': {'required': True, },
        }

    def create(self, validated_data):
        # user = self.context.get('request').user
        user = User.objects.get(id=1)
        price = validated_data['price']
        grade = validated_data['grade']
        comment = validated_data['comment']
        try:
            instance = Rating.objects.get(user=user, price=price)
            instance.grade = grade
            instance.comment = comment
        except Rating.DoesNotExist:
            instance = Rating(user=user, price=price, grade=grade, comment=comment)
        instance.save()
        return instance
