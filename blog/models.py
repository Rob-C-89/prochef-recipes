from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Recipe Post Model
class RecipePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    # Image code to go here
    recipe_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} | by {self.author}"

