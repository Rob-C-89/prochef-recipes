from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from blog.models import RecipePost

# Create your views here.

# View own profile as logged in user.
@login_required
def my_profile(request):
    """Display the logged-in user's profile"""
    profile = request.user.profile_name
    
    # Get all posts by this user
    user_posts = RecipePost.objects.filter(author=request.user).order_by('-date_created')
    
    context = {
        'profile': profile,
        'user_posts': user_posts,
        'posts_count': user_posts.count(),
    }
    
    return render(request, 'profiles/my_profile.html', context)
