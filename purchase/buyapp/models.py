from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Purchase(models.Model):
    """ save all information of each buy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(0|\+)\d{8,11}$',
                                 message="Phone number must be entered in the format: '+219999999' or '0219999999' ."
                                         " Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    address = models.TextField()
    date_time = models.DateField()
    purchase = models.CharField(max_length=150)
    purchase_id = models.IntegerField
    name = models.CharField(max_length=150)
    email = models.EmailField()
