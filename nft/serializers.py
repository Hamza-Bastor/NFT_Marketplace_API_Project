from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from nft.models import Account, Collection, Product

# create classes that will manage the conversion between model and json


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
