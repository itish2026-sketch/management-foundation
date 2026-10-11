from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


# =========================================================
# 1️⃣  NEWS
# =========================================================
class News(models.Model):

    CATEGORY_CHOICES = [
        ('general',     'General'),
        ('announcement','Announcement'),
        ('press',       'Press Release'),
        ('story',       'Success Story'),
        ('update',      'Project Update'),
    ]

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    category    = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='general',
    )

    cover_image = models.ImageField(
        upload_to='news/covers/', blank=True, null=True,
    )

    short_description = models.TextField(
        max_length=350,
        help_text="List page-এ show হবে (max 350 chars)",
    )

    full_content = CKEditor5Field(
        'Full Content',
        config_name='default',
        blank=True,
    )

    author      = models.CharField(max_length=150, blank=True)

    is_featured = models.BooleanField(
        default=False,
        help_text="Check করলে homepage-এ highlight হবে",
    )
    is_active   = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name        = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'news'
            slug = base
            i = 1
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)



# =========================================================
# 2️⃣  EVENTS
# =========================================================
class Event(models.Model):

    STATUS_CHOICES = [
        ('upcoming',  'Upcoming'),
        ('ongoing',   'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    cover_image = models.ImageField(
        upload_to='news/events/', blank=True, null=True,
    )

    short_description = models.TextField(
        max_length=350,
    )

    full_content = CKEditor5Field(
        'Full Description',
        config_name='default',
        blank=True,
    )

    # ---- Location ----
    venue       = models.CharField(max_length=250, blank=True)
    address     = models.CharField(max_length=350, blank=True)

    # ---- Date & Time ----
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField(blank=True, null=True)

    # ---- Organizer ----
    organizer   = models.CharField(max_length=200, blank=True)
    contact     = models.CharField(max_length=200, blank=True)

    # ---- Status ----
    status      = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='upcoming',
    )

    is_featured = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at  = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-start_date']
        verbose_name        = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'event'
            slug = base
            i = 1
            while Event.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)



# =========================================================
# 3️⃣  NOTICES
# =========================================================
class Notice(models.Model):

    PRIORITY_CHOICES = [
        ('normal', 'Normal'),
        ('high',   'High Priority'),
        ('urgent', 'Urgent'),
    ]

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    attachment_pdf = models.FileField(
        upload_to='news/notices/', blank=True, null=True,
        help_text="Optional PDF attachment",
    )

    short_description = models.TextField(
        max_length=300,
    )

    full_content = CKEditor5Field(
        'Full Notice',
        config_name='default',
        blank=True,
    )

    priority    = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='normal',
    )

    # ---- Issuing office ----
    issued_by   = models.CharField(max_length=200, blank=True)

    # ---- Date ----
    published_at = models.DateTimeField(default=timezone.now)
    deadline    = models.DateField(
        blank=True, null=True,
        help_text="Optional deadline / last date",
    )

    is_pinned   = models.BooleanField(
        default=False,
        help_text="Check করলে notice সবার উপরে pinned থাকবে",
    )
    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-is_pinned', '-published_at']
        verbose_name        = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'notice'
            slug = base
            i = 1
            while Notice.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)