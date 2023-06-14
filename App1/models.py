from django.db import models

# Create your models here.
class SignupModels(models.Model):
    memail = models.EmailField()
    mpassword = models.CharField(max_length=20)

    
class UserModels(models.Model):
    memail = models.EmailField()
    mname = models.CharField(max_length=20)
    mage = models.IntegerField()
    mcountry = models.CharField(max_length=20)
    mphone = models.CharField(max_length=10)
    mgender = models.CharField(max_length=10)