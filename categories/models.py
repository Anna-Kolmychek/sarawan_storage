from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, null=False, unique=True, verbose_name='slug')
    preview = models.ImageField(upload_to='categories/', null=False, verbose_name='превью')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, null=False, unique=True, verbose_name='slug')
    preview = models.ImageField(upload_to='subcategories/', null=False, verbose_name='превью')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, related_name='subcategories',
                                 verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
