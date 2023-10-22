from django.contrib import admin

# Register your models here.
from .models import Item,Category

# Register your models here.
@admin.register(Item)

class ItemAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'description','category', 'image' ]


# Register your models here.
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'created_at','created_by' ]