from django.db import models

from common.models import BaseModel


class ImageSize(BaseModel):
    title = models.CharField(max_length=50)
    width = models.FloatField()
    height = models.FloatField()


class Image(BaseModel):
    MEDIA_TYPE = (
        ('PRODUCT', 'PRODUCT'),
        ('SLIDER', 'SLIDER'),
        ('BLOG', 'BLOG'),
    )

    title = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=255)
    type = models.CharField(max_length=24, default='product', choices=MEDIA_TYPE)
    size = models.ForeignKey(ImageSize, on_delete=models.CASCADE)

