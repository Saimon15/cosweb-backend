from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseCategoryModel(BaseModel):
    title = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    class Meta:
        abstract = True
