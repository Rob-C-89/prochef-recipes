from django.contrib import admin
from .models import ContactMessage


# Register ContactMessage model
@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
