from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['preview1', 'preview2', 'preview3', 'category']

    fields = [
        ('title', 'slug'),
        ('subcategory', 'price'),
        ('preview1', 'image1'),
        ('preview2', 'image2'),
        ('preview3', 'image3'),
    ]
    list_display = ['preview1', 'title', 'subcategory', 'category', 'price']
    list_display_links = ['preview1', 'title']

    def preview1(self, obj):
        if not obj.image1:
            return ''
        return mark_safe(f'<img src="{obj.image1.url}" style="max-height: 100px; max_width=100px">')

    def preview2(self, obj):
        if not obj.image2:
            return ''
        return mark_safe(f'<img src="{obj.image2.url}" style="max-height: 100px; max_width=100px">')

    def preview3(self, obj):
        if not obj.image3:
            return ''
        return mark_safe(f'<img src="{obj.image3.url}" style="max-height: 100px; max_width=100px">')

    def category(self, obj):
        return obj.subcategory.category

    preview1.short_description = 'превью1'
    preview2.short_description = 'превью2'
    preview3.short_description = 'превью3'
    category.short_description = 'категория'

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
