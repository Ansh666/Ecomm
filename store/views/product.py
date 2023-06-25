from django.views.generic import ListView
from django.shortcuts import render
from .models import Product


class ProductList(ListView):
    model = Product


def productdetail(request, id):
    product = Product.objects.get(id=id)
    return render(request, '/product.html', {'product': product})
