
from django.shortcuts import render
from .models import ContactMessage
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been sent successfully. "
                "We will get back to you soon.",
            )

    contact_form = ContactForm()

    return render(
        request,
        'contact_us.html',
        {
            'contact_form': contact_form
        },
    )
    