import csv
from datetime import datetime, date
from .models import Expense
from categories.models import ExpensesCategory
from django.contrib.auth.models import User
from django.conf import settings

def import_expense_from_csv(csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if not row['user']:
                print(f"Skipping row due to missing user: {row}")
                continue
            
            try:
                user = User.objects.get(username=row['user'])
            except User.DoesNotExist:
                continue
            
            category, _ = ExpensesCategory.objects.get_or_create(category_name=row['category'], user=user)


            Expense.objects.create(
                user=user,
                name=row['supplier_name'],
                amount=float(row['total_amount']),
                category=category,
                date= row['invoice_date'],
                description=row['description']
            )

def clear_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        header = csv_file.readline()

    with open(csv_file_path, 'w') as csv_file:
        csv_file.write(header)
