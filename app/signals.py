from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog
from django.core.mail import send_mail


from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Blog

@receiver(pre_save, sender=Blog)
def before_save(sender, instance, **kwargs):
    if instance.pk:  # Obyekt hali saqlanmagan bo'lsa, tarjimani olishga urinmaymiz
        print("Bazaga ma'lumot qo'shilishdan oldin:", instance.safe_translation_getter('title', any_language=True))
    else:
        print("Bazaga ma'lumot qo'shilishdan oldin: Yangi obyekt")
        
@receiver(post_save, sender=Blog)
def after_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="365 News saytingizda yangi xabar qo'shildi!",
            message='365 News saytingizda yangi xabar qarab qoying!',
            from_email='biznesssayt365@gmail.com',
            recipient_list=['ismoilerkinov87@gmail.com'],
            fail_silently=False,
        )

