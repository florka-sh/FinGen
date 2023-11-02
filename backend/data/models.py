from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FinanceData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    account_number = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    details = models.CharField( max_length=255)
    withdraw = models.FloatField(null=True)
    deposit = models.FloatField(null=True)
    balance = models.FloatField()
    
    
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    file = models.FileField(upload_to='backend/data/management')
    uploaded_at = models.DateTimeField(auto_now_add=True)