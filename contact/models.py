from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):

    SUBJECT_CHOICES = [
        ('general',   'General Inquiry'),
        ('support',   'Support'),
        ('feedback',  'Feedback'),
        ('complaint', 'Complaint'),
        ('other',     'Other'),
    ]

    name       = models.CharField(max_length=150)
    phone      = models.CharField(max_length=20)
    email      = models.EmailField()
    subject    = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default='general',
    )
    message    = models.TextField()

    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.get_subject_display()}"