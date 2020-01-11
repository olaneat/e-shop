from django.contrib import admin
from .models import UserSignUp
# Register your models here.

@admin.register(UserSignUp)
class SignUpAdmin(admin.ModelAdmin):
	list_field = ['username']