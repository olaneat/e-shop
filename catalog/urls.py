from . import views
from django.urls import path

app_name = 'catlog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/<int:id>', views.product_detail, name='product_detail'),
    path('<slug:category_slug>', views.index, name="category_list")

]
