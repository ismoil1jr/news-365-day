from django.db import models
from parler.models import TranslatableModel,TranslatedFields

# Create your models here.


class Subscribe(models.Model):
    email = models.EmailField(max_length=255,)


class Partner(models.Model):
    logo = models.ImageField(upload_to='partners/')


class Contact(models.Model): 
    instagram = models.URLField()
    telegram = models.URLField()
    youtube = models.URLField()
    phone = models.CharField(max_length=255,)
    email = models.EmailField()
    address = models.CharField(max_length=255,)


class Comment(models.Model):
    name = models.CharField(max_length=255,)
    email = models.EmailField()
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255,)
    message = models.TextField()








    