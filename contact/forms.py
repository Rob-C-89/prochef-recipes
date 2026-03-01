from .models import ContactMessage
from django import forms


class ContactForm(forms.ModelForm):
    """Form for submitting a contact message to site admins."""

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
