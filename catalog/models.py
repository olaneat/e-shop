from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default =0)
    created = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='img')
    price = models.DecimalField(decimal_places=2, max_digits=9)
    available = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catlog:product_detail', args=[self.slug, self.id])

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse("catlog:category_list", args=[self.slug])
    
    

    

