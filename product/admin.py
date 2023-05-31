from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(SizeVarient)
admin.site.register(ColorVarient)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageAdmin,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
