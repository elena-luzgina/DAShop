from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def short_desc(self):
        MAX = 48
        if len(self.description) > MAX:
            return f'{self.description[:MAX]}...'

    def __str__(self):
        return self.name


class Order(models.Model):
    phone = models.CharField(max_length=24)
    email = models.CharField(max_length=128)
    address = models.TextField(blank=True)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def delivery_status(self):
        return 'Delivered' if self.delivered else '...pending...'

    def __str__(self):
        return f'{self.email}'
