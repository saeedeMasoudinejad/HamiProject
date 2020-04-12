from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignupSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class SignupApiModelViewSet(viewsets.ModelViewSet):
    """ register new user"""
    serializer_class = SignupSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer_data = self.get_serializer(data=self.request.data)
        if serializer_data.is_valid():
            password = make_password(serializer_data.validated_data.get('password'))
            return serializer.save(password=password)


