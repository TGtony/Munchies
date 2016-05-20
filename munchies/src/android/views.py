from django.shortcuts import render, get_object_or_404
from random import randint
from django.http import HttpResponseRedirect, HttpResponse
from .SVM.predict import predict_func

import sys
sys.path.insert(0, 'home/ubuntu/Munchies/munchies/src/search/')
from .models import Product




app_name = 'android'

def index(request):
	strr='asf' 	
	return HttpResponse(strr)

def androidQuery(request, adjs):
	query_string = len(adjs)
	query_filter = predict_func(adjs)
	filter_array = query_filter.split()

#	localDbProductIds
	all_product = Product.objects.filter(asin__in=filter_array)
	
	urls=''	
	#for product in all_product:
	#	urls+=product.title
	leng='213'
	return HttpResponse(leng)