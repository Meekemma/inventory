from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'price', 'created_at', 'updated_at') 
    list_filter = ('created_at', 'updated_at')  
    search_fields = ('name', 'description')  
    ordering = ['-created_at'] 
    readonly_fields = ('created_at', 'updated_at')
