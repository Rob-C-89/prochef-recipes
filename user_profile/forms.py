from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Form for creating and updating user profile details."""

    class Meta:
        model = UserProfile
        fields = ['full_name', 'profile_pic', 'recent_role', 'bio']
        widgets = {
            'profile_pic': forms.FileInput(attrs={'accept': 'image/*'}),
        }
