from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.base import ContentFile
from .models import UploadedFile
from django.urls import reverse
import os
from django.conf import settings


class FileUploadViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Use reverse to get the URL for the view.
        self.url = reverse('file_upload-list')  # 'file_upload-list' is the URL name


    def test_file_upload_success(self):
        self.client.force_authenticate(user=self.user)

        # Create a sample file to upload
        file_content = b"Test file content"
        uploaded_file = ContentFile(file_content, name="test_file.txt")

        response = self.client.post(self.url, {'file': uploaded_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_file_upload_failure(self):
        self.client.force_authenticate(user=self.user)

        # Trying to upload without a file should result in a 400 Bad Request
        response = self.client.post(self.url, {}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
