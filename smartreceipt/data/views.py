from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import translation
from random import randint
from operator import attrgetter
from django.http import Http404
import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import ReceiptSerializer, IntegrientSerializer, CategorySerializer

from data.models import Receipt, ReceiptCategory, Integrient, ReceiptIntegrientRelation, ReceiptTopic, ReceiptCategory

def index(request):
	# get all receipts
	receipt_list = Receipt.objects.all
	# get root topics
	topic_list = ReceiptTopic.objects.filter(parentReceiptTopic = None)
	
	return render(request, 'data/index.html', {
		'receipt_list': receipt_list,
		'topic_list': topic_list,
	})
	
def receipts(request):
	# get all receipts
	receipt_list = Receipt.objects.all
	
	return render(request, 'data/receipts.html', {
		'receipt_list': receipt_list,
	})

def receipt(request, receipt_id):
	# get receipt (or fail)
	try:
		receipt = Receipt.objects.get(pk=receipt_id)
	except Receipt.DoesNotExist:
		raise Http404("Receipt does not exist")	
		
	return render(request, 'data/receipt.html', {
		'receipt': receipt,
	})
	
def category(request, category_id):
	try:
		category = ReceiptCategory.objects.get(pk=category_id)
	except ReceiptCategory.DoesNotExist:
		raise Http404("Category does not exist")
		
	receipts = category.receipts()
	
	return render(request, 'data/category.html', {
		'receipts': receipts,
		'category': category,
	})

def categories(request):
	categories = ReceiptCategory.objects.filter(parentReceiptCategory = None)
	
	return render(request, 'data/categories.html', {
		'categories': categories,
	})

def topic(request, topic_id):
	try:
		topic = ReceiptTopic.objects.get(pk=topic_id)
	except ReceiptTopic.DoesNotExist:
		raise Http404("Topic does not exist")
		
	return render(request, 'data/topic.html', {
		'topic': topic,
	})

def integrient_search(request):
	receipt_list = Receipt.objects.all
	integrient_list = Integrient.objects.all()
	
	integrient_name_list = []
	
	for integrient in integrient_list:
		integrient_name = integrient.name
		integrient_name = integrient_name.replace(u'\xdf', '&szlig;')
		integrient_name_list.append(str(integrient_name))
		
	return render(request, 'data/integrient_search.html', {
		'receipt_list': receipt_list,
		'integrient_list': integrient_list,
		'integrient_name_list': integrient_name_list,
	})
	
def receipts_by_integrients(request):

	integrient_names = request.GET.keys()[0].split(',')
	integrients = []
	receipts = []
	
	for integrient in integrient_names:
		integrient_objs = Integrient.objects.filter(name__iexact = integrient)
		if len(integrient_objs):
			integrients.append(integrient_objs[0].id)
			
	for receipt in Receipt.objects.all():
		ranking = 0
		
		for receiptIntegrientRelation in ReceiptIntegrientRelation.objects.filter(receipt = receipt):
			for integrient_id in integrients:
				if receiptIntegrientRelation.integrient.id == integrient_id:
					ranking = ranking + 1
				
		if ranking > 0:
			receiptResult = {}
			receiptResult['receipt_id'] = receipt.id
			receiptResult['receipt_url'] = receipt.url()
			receiptResult['receipt_image_url'] = receipt.image_url()
			receiptResult['receipt_name'] = receipt.name
			receiptResult['receipt_teaser'] = receipt.teaser
			receiptResult['ranking'] = ranking
			receipts.append(receiptResult)

	response_data = {}
	response_data['integrient_names'] = integrient_names
	response_data['integrients'] = integrients
	response_data['receipts'] = receipts
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")
	
def receipts_export(request):
	# get all receipts
	receipt_list = Receipt.objects.all
	categories = ReceiptCategory.objects.filter(parentReceiptCategory = None)
	integrient_list = Integrient.objects.all()
		
	return render(request, 'data/receipts_export.html', {
		'receipt_list': receipt_list,
		'categories' : categories,
		'integrient_list': integrient_list,
	})
	
def export(request):
		
	import os
	os.system('prince --no-author-style --javascript -s http://127.0.0.1:8000/static/data/style_print.css http://127.0.0.1:8000/data/receipts_export/export -o tmp.pdf')
		
	image_data = open('tmp.pdf', "rb").read()
	return HttpResponse(image_data, content_type='application/pdf')
	
    
class RecipesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    
class IntegrientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows integrient to be viewed or edited.
    """
    queryset = Integrient.objects.all()
    serializer_class = IntegrientSerializer
    
class CategorysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows integrient to be viewed or edited.
    """
    queryset = ReceiptCategory.objects.filter(is_country=False)
    serializer_class = CategorySerializer