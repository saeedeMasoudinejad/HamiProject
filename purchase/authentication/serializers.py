from rest_framework import serializers
from django.contrib.auth.models import User



class SignupSerializer(serializers.ModelSerializer):
    """Serializer for register new user and get information"""
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password')
        write_only = 'password'





# class PurchaseSerializer(serializers.ModelSerializer):
#     """ serializer for complete the profile information of user"""
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     first_name = serializers.CharField(max_length=256)
#     last_name = serializers.CharField(max_length=256)
#     class Meta:
#         model = Profile
#         fields = ('user', 'phone_number', 'address', 'first_name', 'last_name')
#
#     def create(self, validated_data):
#         user = self.context['request'].user
#         print(user)
#         phone_number = validated_data['phone_number']
#         address = validated_data['address']
#         profile_instance = Profile.object.create(user=user, phone_number=phone_number, address=address)
#         print(profile_instance)
#         first_name = validated_data['first_name']
#         last_name = validated_data['last_name']
#         user_instance = User.objects.get(username=user)
#         user_instance.first_name = validated_data['first_name']
#         user_instance.last_name = validated_data['last_name']
#         serializers.errors



