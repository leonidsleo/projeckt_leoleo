from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity'] # добавили сортировку
    list_filter = ['date_added', 'price']
    search_fields = ['description'] # поле поиска
    search_help_text = 'Поиск по полю Описание продукта (description)' # подсказка для пользователя


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
