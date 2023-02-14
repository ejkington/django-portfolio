from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            message = f'Name: {name}\nCompany: {company}\nEmail: {email}'
            send_mail(
                'New contact form submission',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
