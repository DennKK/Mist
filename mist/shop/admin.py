from django.contrib import admin
from .models import Genre, Developer, Category, Product, UserProductRelationship


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProductRelationship)