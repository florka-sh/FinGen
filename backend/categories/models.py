from django.db import models
from django.contrib.auth.models import User


class IncomeCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Income category {self.category_name}"

class ExpensesCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Expense category {self.category_name}"


