from django.contrib import admin

from food.models import Food, Price, Category, Packet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [PriceInline, ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    list_display = [
        'price',
        'user',
        'order',
        'number',
    ]
