from django.db import models
from django.contrib.auth.models import User
from blog.models import RecipePost
from cloudinary.models import CloudinaryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile_name')
    profile_pic = CloudinaryField('image', default='#')
    recent_role = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    posts = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name="previous_posts")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s Profile"
