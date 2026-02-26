from django.contrib import admin
from .models import ContactMessage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')