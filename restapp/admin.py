from django.contrib import admin
from .models import Food, RestaurantTable, ContactMessage, Cart, Order, OrderItem
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'meal_time',
        'is_available'
    )
    search_fields = (
        'name',
        'category'
    )
    list_filter = (
        'category',
        'is_available'
    )

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = (
        'table_no',
        'seats',
        'status'
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'table_no',
    )

admin.site.register(ContactMessage)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)