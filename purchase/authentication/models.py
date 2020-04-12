from django.db import models

# class Profile(models.Model):
#     """ save extra information about user"""
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_regex = RegexValidator(regex=r'^(0|\+)\d{8,10}$',
#                                  message="Phone number must be entered in the format: '+219999999' or '0219999999' ."
#                                          " Up to 10 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
#     address = models.TextField()








