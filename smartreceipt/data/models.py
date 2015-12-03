#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.db import models
from django.db.models import Q
from itertools import chain, groupby
from operator import attrgetter
from datetime import date
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from sets import Set
from django.forms import Textarea
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
	class of a integrient type
"""
class IntegrientType(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):			  
		return u'%s' % (self.name)

"""
	class of a integrient
"""
class Integrient(models.Model):
	name = models.CharField(max_length=50)
	type = models.ForeignKey(IntegrientType, blank=True, null=True, related_name="integrient_type") 
	image = models.ImageField(upload_to='media/integrients', blank=True, null=True)
	important = models.NullBooleanField(default=False, blank=True, null=True)

	def thumbnail(self):
		return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="20" /></a>' % ((self.image.name, self.image.name))
	thumbnail.allow_tags = True

	def receipts(self):
		return ReceiptIntegrientRelation.objects.filter(integrient = self)

	def number_of_receipts(self):
		return len(self.receipts())

	def __unicode__(self):			  
		return u'%s' % (self.name)

"""
	class of a receipt
"""
class Receipt(models.Model):
	name = models.CharField(max_length=50)
	teaser = models.CharField(max_length=250, blank=True, null=True)
	description = models.CharField(max_length=20000, blank=True, null=True)
	image = models.ImageField(upload_to='media/receipts', blank=True, null=True)
	time = models.IntegerField(default=0)
	calories = models.IntegerField(default=0)
	portions = models.IntegerField(default=0)
	
	step0 = models.CharField(max_length=1000, blank=True, null=True)
	step1 = models.CharField(max_length=1000, blank=True, null=True)
	step2 = models.CharField(max_length=1000, blank=True, null=True)
	step3 = models.CharField(max_length=1000, blank=True, null=True)
	step4 = models.CharField(max_length=1000, blank=True, null=True)
	step5 = models.CharField(max_length=1000, blank=True, null=True)
	step6 = models.CharField(max_length=1000, blank=True, null=True)
	step7 = models.CharField(max_length=1000, blank=True, null=True)
	step8 = models.CharField(max_length=1000, blank=True, null=True)
	step9 = models.CharField(max_length=1000, blank=True, null=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def url(self):
		return '/data/receipt/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
		
	def image_url(self):
		return '/media/%s' % self.image.name
		
	def time_str(self):
		return u'%d min' % self.time
				
	def categories(self):
		return ReceiptCategoryRelation.objects.filter(receipt = self)
		
	def integrients(self):
		return ReceiptIntegrientRelation.objects.filter(receipt = self)
	
	def steps(self):
		steps = []
		
		if self.step0 is not None:
			steps.append(self.step0)
			
		if self.step1 is not None:
			steps.append(self.step1)
	
		if self.step2 is not None:
			steps.append(self.step2)
	
		return steps
	
	def __unicode__(self):			  
		return u'%s' % (self.name)
	
"""
	class of a ReceiptIntegrientRelation
"""	
class ReceiptIntegrientRelation(models.Model):
	receipt = models.ForeignKey(Receipt)
	integrient = models.ForeignKey(Integrient)
	order = models.IntegerField(default=0)
	amount = models.FloatField(default=0)
	amount_type = models.CharField(max_length=1, choices=(('K', 'Kilogramm'), ('G', 'Gramm'), ('L', 'Liter'), ('M', 'Milliliter'), ('T', 'TL'), ('E', 'EL'), ('S', 'Stück'), ('B', 'Becher'), ('P', 'Prise(n)'), ('C', 'Päckchen'), ('F', 'Flasche(n)'), ('N', 'Scheibe(n)'), ('W', 'Etwas')))
	
	def __unicode__(self):			  
		return u'%s - %s' % (self.receipt.name, self.integrient.name)
	
"""
	class of a ReceiptCategory
"""	
class ReceiptCategory(models.Model):
	name = models.CharField(max_length=50)
	parentReceiptCategory = models.ForeignKey("self", blank=True, null=True)
	image = models.ImageField(upload_to='media/category', blank=True, null=True)
	
	def thumbnail(self):
		return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="20" /></a>' % ((self.image.name, self.image.name))
	thumbnail.allow_tags = True
	
	def path(self):
		if self.parentReceiptCategory is None:
			return self.name
		else:
			return u'%s - %s' % (self.parentReceiptCategory.path(), self.name)
	
	def url(self):
		return '/data/category/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
	
	def children(self):
		return ReceiptCategory.objects.filter(parentReceiptCategory = self)
		
	def receipts(self):
		return ReceiptCategoryRelation.objects.filter(receiptCategory = self)
		
	def number_of_receipts(self):
		num = len(self.receipts())
		
		for child in ReceiptCategory.objects.filter(parentReceiptCategory = self):
			num = num + child.number_of_receipts()
		
		return num
	
	def __unicode__(self):			  
		return u'%s' % (self.path())
		
"""
	class of a ReceiptIntegrientRelation
"""	
class ReceiptCategoryRelation(models.Model):
	receipt = models.ForeignKey(Receipt)
	receiptCategory = models.ForeignKey(ReceiptCategory)
	
	def __unicode__(self):			  
		return u'%s -> %s' % (self.receipt, self.receiptCategory)
		
"""
	class of a ReceiptTopic
"""	
class ReceiptTopic(models.Model):
	name = models.CharField(max_length=50)
	parentReceiptTopic = models.ForeignKey("self", blank=True, null=True)
	
	def path(self):
		if self.parentReceiptTopic is None:
			return self.name
		else:
			return u'%s - %s' % (self.parentReceiptTopic.path(), self.name)
	
	def url(self):
		return '/data/topic/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
	
	def children(self):
		return ReceiptTopic.objects.filter(parentReceiptTopic = self)
		
	def receipts(self):
		return ReceiptTopicRelation.objects.filter(receiptTopic = self)
	
	def __unicode__(self):			  
		return u'%s' % (self.path())
		
"""
	class of a ReceiptTopicRelation
"""	
class ReceiptTopicRelation(models.Model):
	receipt = models.ForeignKey(Receipt)
	receiptTopic = models.ForeignKey(ReceiptTopic)
	
	def __unicode__(self):			  
		return u'%s -> %s' % (self.receipt, self.receiptTopic)