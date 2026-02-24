from .models import Comment, RecipePost
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    
    class Meta:
        model = RecipePost
        fields = ('title', 'image', 'summary', 'recipe_content')

class EditRecipeForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    
    class Meta:
        model = RecipePost
        fields = ('title', 'image', 'summary', 'recipe_content')
