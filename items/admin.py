from django.contrib import admin

# Register your models here.
from .models import Category,Size,Product,Finance,Banner

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
   list_display = ['id','sku', 'barcode', 'name', 'description','category', 'image','size' ,'in_stock','cost','sale_price','status','created_by' , 'created_at']


# Register your models here.
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'created_at','created_by' ]


@admin.register(Size)

class SizeAdmin(admin.ModelAdmin):
   list_display = ['id', 'title', 'created_at','created_by' ]


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
   list_display = ['id', 'invoice_number','cart_cost_price', 'cart_sale_price',  'created_at','created_by' ]



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
   list_display = ['id','image', 'created_at','created_by' ]

