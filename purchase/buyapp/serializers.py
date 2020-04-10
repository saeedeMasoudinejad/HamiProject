from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    """ serializer for serialize purchase information"""
    class Meta:
        model = Purchase
        fields = '__all__'
