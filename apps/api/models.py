from django.db import models
from django.conf import settings
from colorfield.fields import ColorField


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
    description = models.TextField(null=True)

    class Meta:
        abstract = True


class Currency(MetaDataTable):
    country = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=4, null=False)


class Account(MetaDataTable):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, null=False)
    currency = models.ForeignKey(
        Currency, models.DO_NOTHING, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class TypeTransaction(MetaDataTable):
    theme_color = ColorField(default='#FF0000')


class Transaction(DateTable):
    account = models.ForeignKey(
        Account, models.CASCADE,
        related_name='transactions', null=False)
    type = models.ForeignKey(
        TypeTransaction, models.DO_NOTHING, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(null=True)

    class Meta:
        ordering = ['-created_at']
