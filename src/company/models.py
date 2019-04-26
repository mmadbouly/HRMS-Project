from django.db import models

# Create your models here. Django uses MVC model view controller

class CompanyInfo(models.Model):

    COP_CompanyID       = models.IntegerField(default=None ,primary_key=True)
    COP_CompanyName     = models.CharField(max_length=255)
    COP_CompanyAddress  = models.CharField(max_length=255)
    COP_CompanyOwner    = models.CharField(max_length=255)
    COP_DateOfFormation = models.DateField(max_length=8)
    COP_TimeStamp       = models.DateField(auto_now=True)   
