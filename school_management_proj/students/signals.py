from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Fee_status, Students


@receiver(post_save, sender= Students)
def create_fee_challan(sender, instance, created, **kwargs):
    if created:
        now = timezone.now()
        Fee_status.objects.create(
            student = instance,
            amount = instance.fee,
            month = now.strftime("%B"),
            year = now.year
        )