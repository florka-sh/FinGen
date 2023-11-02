from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False, 
        unique=True,
        primary_key=True
    )



    def __str__(self):
        return f'{self.user.username} Profile'


   
    



