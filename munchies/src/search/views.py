from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import TemplateView
from random import randint
from django.http import HttpResponseRedirect, HttpResponse
from .SVM.predict import predict_func


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'search/product_detail.html', {'product': product})


def random(request):
    random_index = randint(1, Product.objects.count())
    return HttpResponseRedirect('/search/' + str(random_index))


class SearchView(TemplateView):
    template_name = "search/search.html"


def results(request):
    if request.GET.get('q'):
        query_string = request.GET['q']
    else:
        query_string = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                       "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                       "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                       "000000000000000000000"
    query_filter = predict_func(query_string)
    filter_array = query_filter.split()
    all_product = Product.objects.filter(asin__in=filter_array)
    return render(request, 'search/results.html', {'all_product': all_product})