from django.contrib import admin
from .models import Genre, Developer, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Product, ProductAdmin)
