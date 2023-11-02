import os
import pandas as pd
from django.core.management.base import BaseCommand, CommandParser, CommandError
from data.models import FinanceData
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import data from Excel or CSV files in a directory to FinanceData model'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("directory", type=str)
        parser.add_argument("file_name", type=str)  # Add an argument for the file name

    def handle(self, *args, **options):
        directory = options.get("directory", None)
        file_name = options.get("file_name", None)

        if not directory or not file_name:
            raise CommandError("Directory or file name not found!")

        if not os.path.isdir(directory):
            raise CommandError("Invalid directory path!")

        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        _, file_extension = os.path.splitext(file_name)
        if file_extension.lower() not in ['.xlsx', '.csv']:
            raise CommandError("Invalid file format!")

        # Read the file into a DataFrame
        if file_extension.lower() == '.xlsx':
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
            df[df.columns[3]] = df[df.columns[3]].str.replace(',', '')
            df[df.columns[4]] = df[df.columns[4]].str.replace(',', '')
            df[df.columns[5]] = df[df.columns[5]].str.replace(',', '')

        df.columns = df.columns.str.replace(' ', '_')
        print(df.columns)

        df.fillna(0, inplace=True)

        # Your data processing and saving logic here
        for row in df.itertuples():
            
            account_number = row[1]
            date = row[2]
            details = row[3]
            withdraw = float(row[4])
            deposit = float(row[5])
            balance = float(row[6])

            # Create and save FinanceData instance
            finance_data = FinanceData(
                user=User.objects.first(),
                account_number=account_number,
                date=date,
                details=details,
                withdraw=withdraw,
                deposit=deposit,
                balance=balance
            )
            finance_data.save()
            