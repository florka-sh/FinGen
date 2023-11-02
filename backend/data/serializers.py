from rest_framework import serializers
from .models import FinanceData, UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('user', 'file', 'uploaded_at')


class FinanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceData
        fields = "__all__"