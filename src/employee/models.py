from django.db import models

# Create your models here. Django uses MVC model view controller

class EmployeeInfo(models.Model):

    EMP_EmployeeID      = models.IntegerField(default=None ,primary_key=True)
    EMP_LastName        = models.CharField(max_length=255)
    EMP_FirstName       = models.CharField(max_length=255)
    EMP_CompanyID       = models.CharField(max_length=255)
    EMP_EmployeeGender  = models.CharField(max_length=255)
    EMP_DateOfBirth     = models.DateField(max_length=8)    # el user by7oto date of birth 3ady
    EMP_TimeStamp       = models.DateField(auto_now=True)   # el user maby7otosh da kol ma y3ml save fel data base
