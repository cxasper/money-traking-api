from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.api.meta_data import TypeTransactionId
from .models import Transaction


@receiver(post_save, sender=Transaction)
def set_amount_account(sender, instance, created, *args, **kwargs):
    if created:
        if instance.type.id == TypeTransactionId.INCOME:
            instance.account.amount += instance.amount
        else:
            instance.account.amount -= instance.amount

        instance.account.save()
