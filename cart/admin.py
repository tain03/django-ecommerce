from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'book', 'quantity', 'created_at']
    list_filter = ['customer', 'created_at']