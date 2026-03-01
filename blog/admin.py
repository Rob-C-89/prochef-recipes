from django.contrib import admin
from .models import RecipePost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):
    """Admin configuration for recipe posts with Summernote editing."""

    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('recipe_content',)


admin.site.register(Comment)
