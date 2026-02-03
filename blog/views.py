from django.shortcuts import render
from django.views import generic
from .models import RecipePost


# Create your views here.
class PostList(generic.ListView):
    queryset = RecipePost.objects.all()
    template_name = "blog/index.html"
