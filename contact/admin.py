from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    """Admin configuration for contact form submissions."""

    list_display = ('name', 'email', 'subject', 'date_sent')
