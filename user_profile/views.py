from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from blog.models import RecipePost
from .forms import UserProfileForm

# Create your views here.

@login_required
def create_profile(request):
    """ Create a user profile for the logged-in user """
    # If user already has a profile, redirect to their profile page
    if hasattr(request.user, 'profile_name'):
        return redirect('my_profile')
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('my_profile')
    else:
        profile_form = UserProfileForm()
    return render(request, 'profiles/create_profile.html', {'profile_form': profile_form})

# Edit profile as logged in user.
@login_required
def edit_profile(request):
    """Allow the logged-in user to edit their profile"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('my_profile')
    else:
        profile_form = UserProfileForm(instance=profile)
    
    return render(request, 'profiles/edit_profile.html', {'profile_form': profile_form})

# View own profile as logged in user.
@login_required
def my_profile(request):
    """Display the logged-in user's profile"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')
    
    # Get all posts by this user
    user_posts = RecipePost.objects.filter(author=request.user).order_by('-date_created')
    
    context = {
        'profile': profile,
        'user_posts': user_posts,
        'posts_count': user_posts.count(),
    }
    
    return render(request, 'profiles/my_profile.html', context)

# View another user's profile by their username.
def view_profile(request, username):
    """Display another user's profile by their username"""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    
    # Get all posts by this user
    user_posts = RecipePost.objects.filter(author=profile.user).order_by('-date_created')
    
    context = {
        'profile': profile,
        'user_posts': user_posts,
        'posts_count': user_posts.count(),
    }
    
    return render(request, 'profiles/profile.html', context)
