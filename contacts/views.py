from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import ContactForm

@require_POST
def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        # Save to database
        contact = form.save()

        # Create email with reply_to
        subject = f"New Email from {contact.name}"
        body = f"Message from {contact.name} <{contact.email}>:\n\n{contact.message}"

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_RECEIVER_EMAIL],
            reply_to=[contact.email],  # This enables Reply-To functionality
        )
        email.send(fail_silently=False)

        messages.success(request, "Your message has been sent successfully!")
    else:
        messages.error(request, "There was a problem with your submission.")

    return redirect('portfolioapp:homepage')
