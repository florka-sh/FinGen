from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "username","first_name", "last_name", "email")
        model = get_user_model()
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



        
        
