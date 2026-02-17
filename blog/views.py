from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import RecipePost, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    queryset = RecipePost.objects.all()
    template_name = "blog/index.html"

def post_detail(request, slug):
    queryset = RecipePost.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


