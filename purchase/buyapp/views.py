from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class PurchaseApiModelViewSet(viewsets.ModelViewSet):
    """ CRUD on purchase model"""
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    # def perform_authentication(self, request):  # TO Do: convert to a middleware
    #     """ for set the user in request"""
    #     token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[0]
    #     data = {'token': token}
    #     try:
    #         valid_data = VerifyJSONWebTokenSerializer().validate(data)
    #         user = valid_data['user']
    #         request.user = user
    #     except ValidationError as v:
    #         print("validation error", v)
