from django.db import models
from django.conf import settings


# Create your models here.
class DateTable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class MetaDataTable(DateTable):
    name = models.CharField(max_length=100, null=False)
    display_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True
