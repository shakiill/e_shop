from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.product.models import Size, Brand, Color, Tag, Category, Product, ProductImage, OrderItem, Order


# Register your models here.
class OrderItemInline(TabularInline):
    model = OrderItem
    fields = ['product', 'unit', 'qty', 'price']
    show_change_link = True
    extra = 0
    fk_name = "order"


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


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, ]
    model = Order
    list_display = ['code', 'student', 'final_amount', 'is_paid']
    list_filter = ['student', 'is_paid']
    search_fields = ['code']


admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductImage)
