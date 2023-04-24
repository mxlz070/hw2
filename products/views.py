from django.shortcuts import render, HttpResponse
from products.models import Product


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouls/index.html')


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'products': product,
            'reviews': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)
