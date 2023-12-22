from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField()

    def __str__(self):
        return f'{self.title}'


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Price(models.Model):
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
        return f'{self.title}'
