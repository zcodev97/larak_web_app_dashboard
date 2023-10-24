from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','invoice_number',
                   'client',
                   'driver',
                   'cart_cost_price',
                   'cart_sale_price',
                   'completed_at',
                   'created_by', 'created_at']

