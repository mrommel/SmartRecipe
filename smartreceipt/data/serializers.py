from django.contrib.auth.models import User, Group
from data.models import Receipt
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = ('name', 'teaser', 'description')