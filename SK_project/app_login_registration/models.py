
from django.db import models
from django.utils import timezone
import datetime
import uuid 



# Create your models here.
class registrationmodel(models.Model):
    memberSponserId = models.AutoField( primary_key = True )
    firstName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    fatherName = models.CharField(max_length=200, null=True)
    dob = models.DateField(default=timezone.now)
    adharCardNumber = models.CharField(max_length=200, null=True)
    penCardNumber = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipCode = models.CharField(max_length=200, null=True)
    nomineName = models.CharField(max_length=200, null=True)
    nominegender = models.CharField(max_length=200, null=True)
    nominedob = models.DateField(default=timezone.now)
    nominePhoneNumber = models.CharField(max_length=200, null=True)
    bankAccountNumber = models.CharField(max_length=200, null=True)
    bankAccountHolder = models.CharField(max_length=200, null=True)
    bankName = models.CharField(max_length=200, null=True)
    ifscCode = models.CharField(max_length=200, null=True)
    branchName = models.CharField(max_length=200, null=True)
    dateTimeCreated = models.DateField(default=datetime.date.today)
    password = models.CharField(max_length=200, null=True)
    sponserId = models.CharField(max_length=200, null=True)


def _str_(self):
    return self.name


