from django.db import models

from common.models import BaseModel


class ProductCategory(BaseModel):
    title = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)


class Product(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
