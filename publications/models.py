from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


# =========================================================
# 1️⃣  ANNUAL REPORT
# =========================================================
class AnnualReport(models.Model):

    title       = models.CharField(
        max_length=250,
        help_text="যেমন: Annual Report 2024",
    )
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    year        = models.CharField(
        max_length=10,
        help_text="যেমন: 2024",
    )

    cover_image = models.ImageField(
        upload_to='publications/reports/', blank=True, null=True,
    )

    summary     = models.TextField(
        max_length=400, blank=True,
        help_text="Short summary for card view (max 400 chars)",
    )

    description = CKEditor5Field(
        'Full Description',
        config_name='default',
        blank=True,
    )

    pdf_file    = models.FileField(
        upload_to='publications/reports/pdf/',
        blank=True, null=True,
        help_text="Main annual report PDF",
    )

    file_size   = models.CharField(
        max_length=20, blank=True,
        help_text="যেমন: 5.2 MB",
    )

    is_featured = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-year', 'display_order']
        verbose_name        = 'Annual Report'
        verbose_name_plural = 'Annual Reports'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'report'
            slug = base
            i = 1
            while AnnualReport.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)



# =========================================================
# 2️⃣  PUBLICATION
# =========================================================
class Publication(models.Model):

    CATEGORY_CHOICES = [
        ('newsletter',   'Newsletter'),
        ('brochure',     'Brochure'),
        ('booklet',      'Booklet'),
        ('research',     'Research Paper'),
        ('manual',       'Manual / Guide'),
        ('magazine',     'Magazine'),
        ('other',        'Other'),
    ]

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    category    = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='other',
    )

    cover_image = models.ImageField(
        upload_to='publications/covers/', blank=True, null=True,
    )

    summary     = models.TextField(
        max_length=400, blank=True,
    )

    description = CKEditor5Field(
        'Full Description',
        config_name='default',
        blank=True,
    )

    pdf_file    = models.FileField(
        upload_to='publications/pdf/', blank=True, null=True,
    )

    file_size   = models.CharField(max_length=20, blank=True)

    author      = models.CharField(max_length=200, blank=True)
    pages       = models.CharField(
        max_length=20, blank=True,
        help_text="যেমন: 48 pages",
    )

    is_featured = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-published_at']
        verbose_name        = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'pub'
            slug = base
            i = 1
            while Publication.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)



# =========================================================
# 3️⃣  DOCUMENT
# =========================================================
class Document(models.Model):

    CATEGORY_CHOICES = [
        ('policy',      'Policy'),
        ('constitution','Constitution'),
        ('guideline',   'Guideline'),
        ('form',        'Form / Application'),
        ('certificate', 'Certificate'),
        ('legal',       'Legal Document'),
        ('other',       'Other'),
    ]

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=280, unique=True, blank=True)

    category    = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='other',
    )

    short_description = models.TextField(max_length=350, blank=True)

    file        = models.FileField(
        upload_to='publications/documents/',
        help_text="PDF / DOC / XLSX file",
    )

    file_type   = models.CharField(
        max_length=20, blank=True,
        help_text="যেমন: PDF, DOCX, XLSX",
    )
    file_size   = models.CharField(max_length=20, blank=True)

    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['display_order', '-uploaded_at']
        verbose_name        = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'doc'
            slug = base
            i = 1
            while Document.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)