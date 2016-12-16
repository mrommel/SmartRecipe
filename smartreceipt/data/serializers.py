from django.contrib.auth.models import User, Group
from data.models import Receipt, ReceiptCategory, ReceiptCategoryRelation, Integrient, IntegrientType, ReceiptCategory
from rest_framework import serializers

class ReceiptIntegrientRelationSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
    	integrients = []
    	
    	for integrient_relation in obj:
    		integrient = dict()
    		integrient['id'] = integrient_relation.integrient.id
    		integrient['quantity'] = integrient_relation.quantity()
    		#integrient['order'] = integrient_relation.order
    		integrients.append(integrient)
    	
    	return integrients
    	
class ReceiptCategoriesRelationSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
    	categories = []
    	
    	for category_relation in obj:
    		if not(category_relation.receiptCategory.is_country):
    	
    			category = dict()
    			category['id'] = category_relation.receiptCategory.id
    			categories.append(category)
    	
    	return categories
        
class CountryCategorySerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
    	name = ''
    	flag = ''
    	has_country = False
    
    	for item in obj:
    		 name = item.name
    		 flag = '/media/%s' % item.image.name
    		 has_country = True
    
    	if has_country:
        	return {
        		'country': {
            		'name': name,
            		'flag': flag
            	}
        	}
        else:
        	return {
        		'country': {
        		}
        	}
       	
class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    countries = CountryCategorySerializer()
    integrients = ReceiptIntegrientRelationSerializer()
    categories = ReceiptCategoriesRelationSerializer()
    
    class Meta:
        model = Receipt
        fields = ('id', 'name', 'teaser', 'description', 'image_url', 'time', 'calories', 'portions', 'steps', 'countries', 'integrients', 'categories', )
        
class IntegrientTypeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = IntegrientType
        fields = ('name', )  
        
class IntegrientSerializer(serializers.HyperlinkedModelSerializer):
    type = IntegrientTypeSerializer()
    
    class Meta:
        model = Integrient
        fields = ('id', 'name', 'type', 'image_url', )
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ReceiptCategory
        fields = ('id', 'path', 'name', 'parent_id', 'number_of_receipts', )  