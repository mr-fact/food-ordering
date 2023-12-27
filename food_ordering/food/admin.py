# food/admin.py

from django.contrib import admin

from account.models import Order
from food.models import Food, Price, Category, Packet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    pass


class PriceInline(admin.TabularInline):
    """
    Inline admin configuration for the Price model.
    """
    model = Price
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Food model.
    """
    inlines = [PriceInline, ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Price model.
    """
    pass


@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Packet model.
    """
    list_display = [
        'price',
        'user',
        'order',
        'number',
    ]


class PacketInline(admin.TabularInline):
    """
    Inline admin configuration for the Packet model in the OrderAdmin.
    """
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
    """
    Admin configuration for the Order model.
    """
    list_display = [
        'user',
    ]
    inlines = [PacketInline, ]
