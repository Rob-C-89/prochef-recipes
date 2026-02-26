from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import RecipePost, Comment
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, RecipeForm


# Post list view to show all recipes on the home page.
class PostList(generic.ListView):
    queryset = RecipePost.objects.all()
    template_name = "blog/index.html"
    paginate_by = 8


# Post detail view to show the details of a recipe and its comments.
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


# Post recipe as logged in user.
@login_required
def post_recipe(request):
    """ View to post a recipe. """
    user_profile_exists = UserProfile.objects.filter(
        user=request.user).exists()
    if not user_profile_exists:
        messages.add_message(
            request,
            messages.ERROR,
            "Create a profile before posting a recipe.",
        )
        return redirect('create_profile')

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_post = recipe_form.save(commit=False)
            recipe_post.author = request.user
            recipe_post.slug = slugify(recipe_post.title)
            recipe_post.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Recipe posted successfully.")
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(
        request,
        'blog/post_recipe.html',
        {'recipe_form': recipe_form, 'user_profile_exists': True},
    )


# Edit recipe as logged in author.
@login_required
def edit_recipe(request, pk):
    """ View to edit a recipe. """
    recipe_post = get_object_or_404(RecipePost, pk=pk)

    if request.user != recipe_post.author:
        messages.add_message(request, messages.ERROR,
                             "You do not have permission to edit this recipe.")
        return redirect('home')

    if request.method == 'POST':
        recipe_form = RecipeForm(
            request.POST, request.FILES, instance=recipe_post)
        if recipe_form.is_valid():
            edited_recipe = recipe_form.save(commit=False)
            edited_recipe.slug = slugify(edited_recipe.title)
            edited_recipe.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Recipe updated successfully.")
            return redirect('post_detail', slug=edited_recipe.slug)
    else:
        recipe_form = RecipeForm(instance=recipe_post)

    return render(request, 'blog/edit_recipe.html',
                  {'recipe_form': recipe_form, 'recipe_post': recipe_post})


# Delete recipe as logged in author.
@login_required
def delete_recipe(request, pk):
    """ View to delete a recipe. """
    recipe_post = get_object_or_404(RecipePost, pk=pk)

    if request.user != recipe_post.author:
        messages.add_message(request, messages.ERROR,
                             "You do not have permission "
                             "to delete this recipe.")
        return redirect('home')

    recipe_post.delete()
    messages.add_message(request, messages.SUCCESS,
                         "Recipe deleted successfully.")
    return redirect('home')


# Delete comment as logged in user.
@login_required
def delete_comment(request, slug, comment_id):
    """ Delete a comment if the logged in user is the author of the comment."""
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             "Comment deleted successfully.")
    else:
        messages.add_message(
            request, messages.ERROR, "You do not have permission "
            "to delete this comment.")

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
