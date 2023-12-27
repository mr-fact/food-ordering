from django.db import models

from account.models import User, Order


class Category(models.Model):
    """
    Model representing a category of food items.
    """
    title = models.CharField(max_length=255)
    # image = models.ImageField()

    def __str__(self):
        return f'{self.title}'


class Food(models.Model):
    """
    Model representing a food item.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Price(models.Model):
    """
    Model representing the pricing information for a food item.
    """
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='prices')
    short_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    init_price = models.IntegerField(blank=True, null=True, default=None)
    price = models.IntegerField()
    ACTIVE = 1
    INACTIVE = 2
    HIDDEN = 3
    STATUS = (
        (ACTIVE, 'قابل فروش'),
        (INACTIVE, 'قابل مشاهده و غیر قابل فروش'),
        (HIDDEN, 'غیر قابل مشاهده'),
    )
    status = models.SmallIntegerField(choices=STATUS, default=ACTIVE)

    def __str__(self):
        return f'{self.food.name}({self.title})'


class Packet(models.Model):
    """
    Model representing a packet, which is a collection of items that a user can order.
    """
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='packets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packets')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='packets',
                              null=True, blank=True, default=None
                              )
    number = models.IntegerField(default=0)

    @classmethod
    def get_or_create(cls, user, price):
        """
        Get or create a packet for the given user and price.
        """
        try:
            packet = cls.objects.get(price=price, user=user, order=None)
        except Packet.DoesNotExist:
            packet = Packet(
                price=price,
                user=user
            )
            packet.save()
        return packet

    @classmethod
    def plus_1(cls, user, price):
        """
        Increase the quantity of items in a packet by 1.
        """
        packet = cls.get_or_create(user, price)
        packet.number += 1
        packet.save()
        return packet

    @classmethod
    def minus_1(cls, user, price):
        """
        Decrease the quantity of items in a packet by 1.
        If the quantity becomes 0 or less, delete the packet.
        """
        packet = cls.get_or_create(user, price)
        packet.number -= 1
        packet.save()
        if packet.number <= 0:
            packet.delete()
            return None
        return packet
