from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework.permissions import IsAuthenticated


class PurchaseApiModelViewSet(viewsets.ModelViewSet):
    """ CRUD on purchase model"""
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


