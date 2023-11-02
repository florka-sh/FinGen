from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from categories.models import ExpensesCategory
from .models import Expense
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class ExpensesTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
                "username": "testUser",
                "email": "test@email.com",
                "password1": "123test123",
                "password2": "123test123"
            }
    
        self.category_data = {
                "category_name": "test_category",
                "description": "My test category",
                "user": 1
            }
        
        self.expense_data = {
                "name": "Test expence",
                "amount": 200.0,
                "date": datetime.now(tz=timezone.utc),
                "description": "My test expense description",
                "user": 1,
                "category": 1
            }
        
        self.user = self.client.post("/customer/rest-auth/registration/", self.user_data)
        last_user_id = User.objects.last().id
        self.expense_data['user'] = last_user_id
        self.category_data['user'] = last_user_id
        
        self.category = self.client.post("/categories/expenses-category/", self.category_data).json()
        self.expense_data['category'] = ExpensesCategory.objects.last().id
        
        self.user = self.client.post('/customer/rest-auth/login/', {"username": self.user_data["username"], "email": self.user_data['email'], "password": self.user_data['password1']})

        
    def test_creation(self):
        expense = self.client.post("/expenses/", self.expense_data).json()
        
        self.assertEqual(expense["name"], self.expense_data['name'])
        self.assertEqual(float(expense["amount"]), self.expense_data['amount'])
        self.assertEqual(expense["date"], self.expense_data['date'].strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertEqual(expense["description"], self.expense_data['description'])
        self.assertEqual(expense["user"], self.expense_data['user'])
        
        
    def test_retrieving(self):
        self.client.post("/expenses/", self.expense_data)
        self.client.post("/expenses/", self.expense_data)
        self.client.post("/expenses/", self.expense_data)

        expenses = self.client.get("/expenses/").json()
        
        self.assertEqual(len(expenses), 3)
        
    def test_update(self):
        expense = self.client.post("/expenses/", self.expense_data).json()
        
        self.changed_expense_data = self.expense_data.copy()
        
        patched_expense = self.client.patch(f"/expenses/{expense['id']}/", 
                          {"name": "My PATCHed expense", 
                           "description": "This is result of changing expense entity"}).json()
        
        self.assertEqual(patched_expense["name"], "My PATCHed expense")
        self.assertEqual(patched_expense["description"], "This is result of changing expense entity")
        
        
    def test_deletion(self):
        expense = self.client.post("/expenses/", self.expense_data).json()
        expense1 = self.client.post("/expenses/", self.expense_data).json()
        
        self.assertEqual(Expense.objects.count(), 2)
                
        self.client.delete(f"/expenses/{expense1['id']}/")        
        self.assertEqual(Expense.objects.count(), 1)
        
        self.client.delete(f"/expenses/{expense['id']}/")
        self.assertEqual(Expense.objects.count(), 0)


class ExpensesViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.upload_receipt_url = reverse('expenses-upload-receipt')

    def test_upload_receipt_valid(self):
        with open('expenses/test_files/test_image.jpg', 'rb') as receipt_image:
            response = self.client.post(self.upload_receipt_url, {'receipt_image': receipt_image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Expense receipt processed successfully.')

    def test_upload_receipt_invalid_file_type(self):
        with open('expenses/test_files/test_file.txt', 'rb') as invalid_file:
            response = self.client.post(self.upload_receipt_url, {'receipt_image': invalid_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid form submission.')