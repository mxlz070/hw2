from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from .constans import PAGINATION_LIMIT


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search_text:
            products = products.filter(title__icontains=search_text)
        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouls/index.html')


def product_detail_view(request, id, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.review_set.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                products_id=kwargs['id']
            )
            product = Product.objects.get(id=kwargs['id'])
            context = {
                'product': product,
                'comment': Review.objects.filter(products_id=kwargs['id']),
                'form': ReviewCreateForm
            }
            return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/products_create.html', context=data)

    else:
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                # image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )

            return redirect('/products')
        else:
            data = {
                'form': form
            }

        return render(request, 'products/products_create.html', context=data)
