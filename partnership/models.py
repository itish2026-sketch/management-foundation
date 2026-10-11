from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Partner(models.Model):

    CATEGORY_CHOICES = [
        ('government',   'Government'),
        ('ngo',          'NGO / Non-Profit'),
        ('international','International'),
        ('corporate',    'Corporate'),
        ('community',    'Community Organization'),
        ('other',        'Other'),
    ]

    name        = models.CharField(max_length=250)
    logo        = models.ImageField(
        upload_to='partnership/logos/', blank=True, null=True,
    )
    category    = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='ngo',
    )
    short_description = models.CharField(
        max_length=300, blank=True,
        help_text="এক লাইনের পরিচিতি (max 300 chars)",
    )
    full_description = CKEditor5Field(
        'Full Description',
        config_name='default',
        blank=True,
    )
    website     = models.URLField(blank=True)
    since_year  = models.CharField(
        max_length=10, blank=True,
        help_text="যেমন: 2014",
    )
    location    = models.CharField(max_length=200, blank=True)

    is_featured = models.BooleanField(
        default=False,
        help_text="Check করলে homepage-এ highlight হবে",
    )
    is_active   = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at  = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name        = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name


class PartnershipInfo(models.Model):
    """
    Page-এর header/intro section — একটাই instance থাকবে।
    (Singleton pattern)
    """

    heading     = models.CharField(
        max_length=250,
        default="Partnership & Membership",
    )
    sub_heading = models.CharField(
        max_length=400, blank=True,
        default="Working together for sustainable development",
    )
    intro_text  = CKEditor5Field(
        'Intro Text',
        config_name='default',
        blank=True,
    )
    background_image = models.ImageField(
        upload_to='partnership/hero/', blank=True, null=True,
    )

    class Meta:
        verbose_name        = 'Partnership Page Info'
        verbose_name_plural = 'Partnership Page Info'

    def __str__(self):
        return self.heading


class PartnershipBenefit(models.Model):
    """
    "Why Partner With Us" section-এর কার্ড
    """

    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon        = models.CharField(
        max_length=100,
        default='bi-handshake',
        help_text="Bootstrap icon class (যেমন: bi-handshake)",
    )
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name        = 'Partnership Benefit'
        verbose_name_plural = 'Partnership Benefits'

    def __str__(self):
        return self.title


class PartnershipTimeline(models.Model):
    """
    Timeline entries — কবে থেকে কোন partner
    """

    year        = models.CharField(max_length=10)
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'year']
        verbose_name        = 'Timeline Entry'
        verbose_name_plural = 'Timeline Entries'

    def __str__(self):
        return f"{self.year} — {self.title}"


class PartnershipStat(models.Model):
    """
    Statistics — যেমন "১৫+ Partner", "১০০+ Projects"
    """

    label = models.CharField(max_length=150)
    value = models.CharField(max_length=50)
    icon  = models.CharField(
        max_length=100, default='bi-people',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name        = 'Statistic'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return f"{self.value} — {self.label}"