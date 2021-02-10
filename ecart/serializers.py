from rest_framework import serializers
from ecart.models import ecart, categorymap

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categorymap

class ecartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ecart
        category_id = categorySerializer(read_only = True, many = True)
        fields = ['id', 'name', 'quantity', 'category_id']

        