from django.shortcuts import render, redirect
from django.contrib import messages as dj_messages
from django.utils import timezone

from .forms import ContactForm
from .models import ContactMessage
from .utils import generate_contact_pdf


def contact_view(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.created_at = timezone.now()
            instance.save()

            # Auto PDF generate
            try:
                generate_contact_pdf(instance)
            except Exception as e:
                print(f"[PDF ERROR] {e}")

            dj_messages.success(
                request,
                'আপনার বার্তা সফলভাবে পাঠানো হয়েছে। আমরা শীঘ্রই যোগাযোগ করব।'
            )

            return redirect('contact:contact')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})