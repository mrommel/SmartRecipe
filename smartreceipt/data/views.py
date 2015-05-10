from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import translation
from random import randint
from operator import attrgetter
from django.http import Http404
import json

from data.models import Receipt, ReceiptCategory, Integrient, ReceiptIntegrientRelation, ReceiptTopic

def index(request):
	# get all receipts
	receipt_list = Receipt.objects.all
	# get root topics
	topic_list = ReceiptTopic.objects.filter(parentReceiptTopic = None)
	# load template
	template = loader.get_template('data/index.html')
	# prepare context
	context = RequestContext(request, { 
		'receipt_list': receipt_list,
		'topic_list': topic_list,
	})
	return HttpResponse(template.render(context))
	
def receipts(request):
	# get all receipts
	receipt_list = Receipt.objects.all
	# load template
	template = loader.get_template('data/receipts.html')
	# prepare context
	context = RequestContext(request, { 
		'receipt_list': receipt_list,
	})
	return HttpResponse(template.render(context))

def receipt(request, receipt_id):
	# get receipt (or fail)
	try:
		receipt = Receipt.objects.get(pk=receipt_id)
	except Receipt.DoesNotExist:
		raise Http404("Receipt does not exist")	
	# load template
	template = loader.get_template('data/receipt.html')
	# prepare context
	context = RequestContext(request, {
		'receipt': receipt,
	})
	return HttpResponse(template.render(context))
	
def category(request, category_id):
	try:
		category = ReceiptCategory.objects.get(pk=category_id)
	except ReceiptCategory.DoesNotExist:
		raise Http404("Category does not exist")
		
	receipts = category.receipts()
	# load template
	template = loader.get_template('data/category.html')
	# prepare context
	context = RequestContext(request, {
		'receipts': receipts,
		'category': category,
	})
	return HttpResponse(template.render(context))

def categories(request):
	categories = ReceiptCategory.objects.filter(parentReceiptCategory = None)
	# load template
	template = loader.get_template('data/categories.html')
	# prepare context
	context = RequestContext(request, {
		'categories': categories,
	})
	return HttpResponse(template.render(context))

def integrient_search(request):
	receipt_list = Receipt.objects.all
	integrient_list = Integrient.objects.all()
	
	integrient_name_list = []
	
	for integrient in integrient_list:
		integrient_name = integrient.name
		integrient_name = integrient_name.replace(u'\xdf', '&szlig;')
		integrient_name_list.append(str(integrient_name))
	# load template
	template = loader.get_template('data/integrient_search.html')
	# prepare context
	context = RequestContext(request, { 
		'receipt_list': receipt_list,
		'integrient_list': integrient_list,
		'integrient_name_list': integrient_name_list,
	})
	return HttpResponse(template.render(context))
	
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
	
		