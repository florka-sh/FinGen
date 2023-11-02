from datetime import datetime ,date
from django.db import models
from django.contrib.auth.models import User
from categories.models import ExpensesCategory

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="New expense")
    amount = models.FloatField(default=0)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Expense {self.name} - {self.category.category_name}"
