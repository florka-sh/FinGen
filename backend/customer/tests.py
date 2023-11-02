from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='dciuser',
            password='dcipassword'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            image='my_image.jpg'
        )

    def test_profile_creation(self):
        """Test if a profile is created correctly."""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.image, 'my_image.jpg')
        
    def test_profile_update(self):
        """Test updating a profile."""
        updated_image = 'new_image.jpg'
        self.profile.image = updated_image
        self.profile.save()
        updated_profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(updated_profile.image, updated_image)
        
    def test_profile_deletion(self):
        """Test deleting a profile."""
        profile_uuid = self.profile.uuid  
        self.profile.delete()
        try:
            deleted_profile = Profile.objects.get(uuid=profile_uuid)
        except Profile.DoesNotExist:
            deleted_profile = None
        self.assertIsNone(deleted_profile)
