from django.contrib import admin

from account.models import Order
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


class PacketInline(admin.TabularInline):
    model = Packet
    fields = [
        'price',
        'number',
    ]

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
    ]
    inlines = [PacketInline, ]
