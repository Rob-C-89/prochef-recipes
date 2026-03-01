from .models import Comment, RecipePost
from django import forms


class CommentForm(forms.ModelForm):
    """Form for submitting a comment on a recipe post."""

    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """Form for creating a new recipe post."""

    class Meta:
        model = RecipePost
        fields = ('title', 'image', 'summary', 'recipe_content')


class EditRecipeForm(forms.ModelForm):
    """Form for editing an existing recipe post."""

    class Meta:
        model = RecipePost
        fields = ('title', 'image', 'summary', 'recipe_content')
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
