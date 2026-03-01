from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    """Render and process the contact form submission."""
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
