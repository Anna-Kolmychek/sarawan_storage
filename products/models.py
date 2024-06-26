from django.db import models

from categories.models import SubCategory


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, verbose_name='продукт')
    slug = models.SlugField(max_length=200, unique=True, null=False, verbose_name='slug')
    image1 = models.ImageField(upload_to='products', verbose_name='картинка 1', null=True, blank=True)
    image2 = models.ImageField(upload_to='products', verbose_name='картинка 2', null=True, blank=True)
    image3 = models.ImageField(upload_to='products', verbose_name='картинка 3', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='цена')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False,
                                    verbose_name='подкатегория',
                                    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def subcategory_title(self):
        return self.subcategory.title

    def category_title(self):
        return self.subcategory.category.title
