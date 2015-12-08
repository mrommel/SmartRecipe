from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from data.models import IntegrientType, Integrient, Receipt, ReceiptIntegrientRelation, ReceiptCategoryRelation, ReceiptCategory

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ReceiptIntegrientRelationInline(admin.TabularInline):
	model = ReceiptIntegrientRelation
	fk_name = "receipt"
	extra = 4
	
	def get_extra (self, request, obj=None, **kwargs):
		""" hide all extra if the current user is having the wrong gender """
		return 5
		#try:
		#	person_id = request.path.replace('/admin/data/person/', '').replace('/', '')
		#	if person_id <> 'add':
		#		person = Person.objects.get(id = person_id)
		#		if person.sex == 'F':
		#			return 0
		#except Person.DoesNotExist:
		#	pass
		
		"""Dynamically sets the number of extra forms. 0 if the related object
		already exists or the extra configuration otherwise."""
		if obj:
			# Don't add any extra forms if the related object already exists.
			return 1
		return self.extra

class ReceiptCategoryRelationInline(admin.TabularInline):
	model = ReceiptCategoryRelation
	fk_name = "receipt"
	extra = 4
	
	def get_extra (self, request, obj=None, **kwargs):
		""" hide all extra if the current user is having the wrong gender """
		return 5
		#try:
		#	person_id = request.path.replace('/admin/data/person/', '').replace('/', '')
		#	if person_id <> 'add':
		#		person = Person.objects.get(id = person_id)
		#		if person.sex == 'F':
		#			return 0
		#except Person.DoesNotExist:
		#	pass
		
		"""Dynamically sets the number of extra forms. 0 if the related object
		already exists or the extra configuration otherwise."""
		if obj:
			# Don't add any extra forms if the related object already exists.
			return 1
		return self.extra
		
class ReceiptCategoryRelationInline2(admin.TabularInline):
	model = ReceiptCategoryRelation
	fk_name = "receiptCategory"
	extra = 0
	
	def get_extra (self, request, obj=None, **kwargs):
		""" hide all extra if the current user is having the wrong gender """
		return 0
		
class ReceiptAdminForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('name', 'teaser', 'description', 'image', 'time', 'calories', 'portions', 
        	'step0', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9')
        widgets = {
            'teaser': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step0': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step1': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step2': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step3': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step4': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step5': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step6': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step7': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step8': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step9': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }

class ReceiptAdmin(admin.ModelAdmin):
    form = ReceiptAdminForm
    ordering = ('name',)
    inlines = [
        ReceiptIntegrientRelationInline,
        ReceiptCategoryRelationInline,
    ]
    actions_on_top = True
    actions_on_bottom = True
        
    class Media:
        css = {
            'all': ('data/css/admin.css',)
        }
        
class IntegrientAdmin(admin.ModelAdmin):
	model = Integrient
	list_display = ('name', 'thumbnail',  'type', 'important')
	ordering = ('name',)

class ReceiptCategoryAdmin(admin.ModelAdmin):
    model = ReceiptCategory
    list_display = ('thumbnail', 'name', 'path', )
    readonly_fields = ('thumbnail', 'path', )
    ordering = ('name',)
    
    inlines = [
        ReceiptCategoryRelationInline2,
    ]
