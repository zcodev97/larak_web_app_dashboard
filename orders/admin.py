from django.contrib import admin
from .models import Order,Cart
from items.models import Product
# Register your models here.
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','invoice_number',
                   'client',
                   'cart',
                   'driver',
                   'cart_cost_price',
                   'cart_sale_price',
                    'created_at',
                   'completed_at']


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'created_at', 'display_cart_items']

    # def display_products(self, obj):
    #     return ", ".join([cart_items.name for cart_items in obj.Products.all()])
    # display_products.short_description = 'Products'

    def display_cart_items(self, obj):
        return ", ".join([str(item) for item in obj.cart_items.all()])

    display_cart_items.short_description = 'Cart Items'