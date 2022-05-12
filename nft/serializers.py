from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from nft.models import Register, Collection, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = '__all__'
