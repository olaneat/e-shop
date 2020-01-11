from . import views
from django.urls import path

app_name = 'register'
urlpatterns = [
    path('registration', views.signUp, name="signup"),
    path('login', views.user_login, name="user_login"),
]

