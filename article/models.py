from django.db import models

from common.models import BaseModel


class ArticleCategory(BaseModel):
    title = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)


class Article(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    image = models.ImageField()
