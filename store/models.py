from django.db import models
from django.urls import reverse

from accounts.models import Accounts
from category.models import Category
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    artist = models.CharField(max_length=50,blank=True)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])


class ReviewRating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    subject = models.CharField(max_length=500,blank=True)
    review = models.TextField(max_length=100,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject