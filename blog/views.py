from django.shortcuts import render # type: ignore
from django.http import HttpResponse, JsonResponse
from .models import Product
def home(req):
    products = Product.objects.all()
    return render(req, 'product.html', context={'products': products})

def product_detail(req, pk):
    product = Product.objects.get(pk=pk)
    # product = Product.objects.all(pk=pk)
    return render(req, 'product_detail.html', { 'product': product })
def err_404_not_found(req):
    return render(req, '404.html')