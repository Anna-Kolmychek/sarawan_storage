from django.contrib import admin
from django.utils.safestring import mark_safe

from categories.models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['preview_img']

    fields = [('title', 'slug'), ('preview', 'preview_img')]
    list_display = ['preview_img', 'title']
    list_display_links = ['preview_img', 'title']

    def preview_img(self, obj):
        return mark_safe(f'<img src="{obj.preview.url}" style="max-height: 100px; max_width=100px">')

    preview_img.short_description = 'превью'

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ['preview_img']

    fields = [('title', 'slug'), 'category', ('preview', 'preview_img')]
    list_display = ['preview_img', 'title']
    list_display_links = ['preview_img', 'title']

    def preview_img(self, obj):
        return mark_safe(f'<img src="{obj.preview.url}" style="max-height: 100px; max_width=100px">')

    preview_img.short_description = 'превью'

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
