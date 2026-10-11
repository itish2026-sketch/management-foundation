from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# ⬇️ Import CKEditor 5 field
from django_ckeditor_5.fields import CKEditor5Field


class WhatWeDo(models.Model):

    CATEGORY_CHOICES = [
        ('education',   'Education'),
        ('health',      'Health'),
        ('community',   'Community Development'),
        ('ongoing',     'Ongoing Program Activities'),
        ('other',       'Other'),
    ]

    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=220, unique=True, blank=True)

    category    = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
    )

    # ⬇️ Simple text (300 chars summary) — এটা normal TextField-ই থাকবে
    short_description = models.TextField(
        max_length=300,
        help_text="Post list-এ দেখানোর জন্য short summary (max 300 chars)",
    )

    cover_image = models.ImageField(
        upload_to='whatwedo/covers/',
        blank=True,
        null=True,
        help_text="Post-এর main cover image",
    )

    is_active   = models.BooleanField(
        default=True,
        help_text="Uncheck করলে post website-এ show হবে না",
    )

    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'What We Do Post'
        verbose_name_plural = 'What We Do Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'post'
            slug = base_slug
            counter = 1
            while WhatWeDo.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class WhatWeDoBlock(models.Model):
    """
    প্রতিটা post-এর ভেতরে multiple content blocks:
    Text (Rich Text) → Image → Text (Rich Text) → Image ...
    """

    post      = models.ForeignKey(
        WhatWeDo,
        on_delete=models.CASCADE,
        related_name='blocks',
    )

    # ⬇️ CKEditor 5 — Rich Text with full formatting + image upload
    text      = CKEditor5Field(
        'Text',
        config_name='default',  # 'extends' বা 'default'
        blank=True,
    )

    image     = models.ImageField(
        upload_to='whatwedo/blocks/',
        blank=True,
        null=True,
    )
    order     = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name        = 'Content Block'
        verbose_name_plural = 'Content Blocks'

    def __str__(self):
        return f"Block #{self.order} — {self.post.title}"