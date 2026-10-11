from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Rahila Begum',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '01XXXXXXXXX',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@gmail.com',
                'class': 'form-input',
            }),
            'subject': forms.Select(attrs={
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Describe your question or problem in detail...',
                'rows': 5,
                'class': 'form-input',
            }),
        }

        labels = {
            'name':    'Your Name',
            'phone':   'Phone Number',
            'email':   'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }