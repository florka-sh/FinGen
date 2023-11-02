import csv
from datetime import datetime
from .models import Income
from categories.models import IncomeCategory
from django.contrib.auth.models import User
from django.conf import settings

def import_income_from_csv(csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if not row['user']:
                print(f"Skipping row due to missing user: {row}")
                continue
            
            try:
                user = User.objects.get(username=row['user'])
            except User.DoesNotExist:
                print(f"User {row['user']} does not exist. Skipping row: {row}")
                continue
            
            category, _ = IncomeCategory.objects.get_or_create(category_name=row['category'], user=user)

            Income.objects.create(
                user=user,
                name=row['income_source'],
                amount=float(row['amount']),
                category=category,
                date=row['date'],
                description=row['category'] 
            )


def clear_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        header = csv_file.readline()

    with open(csv_file_path, 'w') as csv_file:
        csv_file.write(header)

