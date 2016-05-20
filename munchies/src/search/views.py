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

def androidQuery(request, adjs):
	query_string = len(adjs)
	query_filter = predict_func(adjs)
#	filter_array = query_filter.split()

#	localDbProductIds
#	all_product = Product.objects.filter(asin__in=filter_array)
	
#	urls=''	
#	for product in all_product:
#		urls+='['
#		urls+=product.title
#		urls+='/'
#		urls+=product.url
#		urls+=' '
#		urls+=product.asin
		
	return HttpResponse(query_filter)





def asinQry(request, asin):
	asin=asin.replace("_"," ")
	
	filter_array = asin.split()
	all_product = Product.objects.filter(asin__in=filter_array)

	urls=''	
	for product in all_product:
		urls+=product.url
		urls+='_'
		urls+=product.title
		urls+='_'
		urls+=product.description
		urls+='_'		
	return HttpResponse(urls)







