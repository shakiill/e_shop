from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.product.models import Size, Brand, Color, Tag, Category, Product, ProductImage


# Register your models here.
class ProductImageInline(TabularInline):
    model = ProductImage
    fields = ['image']
    show_change_link = True
    extra = 0
    fk_name = "product"


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    model = Product
    list_display = ['title', 'slug', 'category', 'brand']
    list_filter = ['category', 'brand']
    search_fields = ['title']


admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
