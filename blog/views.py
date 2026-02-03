from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import RecipePost


# Create your views here.
class PostList(generic.ListView):
    queryset = RecipePost.objects.all()
    template_name = "blog/index.html"

def post_detail(request, slug):
    queryset = RecipePost.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
