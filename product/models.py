from django.db import models
import uuid
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="categories")
    category_slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name


class SizeVarient(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product_value = models.IntegerField(default=0)
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name


class ColorVarient(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product_value = models.IntegerField(default=0)
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name


class Product(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    category_uid = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    product_value = models.IntegerField()
    product_desc = models.TextField()
    product_slug = models.SlugField(unique=True, blank=True, null=True)
    color_uid = models.ManyToManyField(ColorVarient, blank=True)
    size_uid = models.ManyToManyField(SizeVarient, blank=True)

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name


class ProductImage(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product_uid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    product_images = models.ImageField(upload_to="products")
