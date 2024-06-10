from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    catalog_ob = Phone.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'max_price':
        catalog_ob = catalog_ob.order_by('price').reverse()
    elif sort_by == 'min_price':
        catalog_ob = catalog_ob.order_by('price')
    elif sort_by == 'name':
        catalog_ob = catalog_ob.order_by('name')


    return render(request, 'catalog.html', {'catalog': catalog_ob})



def show_product(request, slug):
    product_ob = Phone.objects.get(slug=slug)
    return render(request, 'product.html', {'product': product_ob})


