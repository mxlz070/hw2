from django.shortcuts import render
from products.models import Product


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        """"""

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouls/index.html')
