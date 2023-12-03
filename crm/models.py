from django.db import models

# Create your models here.
class Renter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=100)
  telephone = models.CharField(max_length= 10)
  gender = models.CharField(max_length=15)