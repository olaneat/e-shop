from django.shortcuts import render, get_object_or_404
from.models import Product, Category
# Create your views here.

def index(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        product = product.filter(category = category)
    return render(request, 'catlog/indexs.html', {
        'categories': categories,
        'product': product,
        'category': category})







def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id, available=True)
    return render(request, 'catlog/product_detail.html', {'product': product})

