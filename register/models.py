from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class UserSignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=150)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta: 
        ordering = ('-user',)
        verbose_name = 'Registered User'
        verbose_name_plural = 'Registered Users'
    
