from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from blog.models import RecipePost
from .forms import UserProfileForm

# Create your views here.

@login_required
def create_profile(request):
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
