from django.db import models


class ContactMessage(models.Model):
    """Stores a contact form message submitted by a site visitor."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=200)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - Subject: {self.subject}"
