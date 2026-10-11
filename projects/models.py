from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field


class Project(models.Model):

    # =========================================================
    # CHOICES
    # =========================================================
    STATUS_CHOICES = [
        ('ongoing',   ' Ongoing'),
        ('completed', ' Completed'),
        ('upcoming',  ' Upcoming'),
        ('suspended', ' Suspended'),
    ]

    CATEGORY_CHOICES = [
        ('education',  'Education'),
        ('health',     'Health'),
        ('community',  'Community Development'),
        ('livelihood', 'Livelihood'),
        ('water',      'Water & Sanitation'),
        ('agriculture','Agriculture'),
        ('other',      'Other'),
    ]

    PROJECT_TYPE_CHOICES = [
        ('short', 'Short Term'),
        ('long',  'Long Term'),
    ]


    # =========================================================
    # BASIC INFO
    # =========================================================
    project_name    = models.CharField(max_length=250)
    slug            = models.SlugField(max_length=280, unique=True, blank=True)

    project_code    = models.CharField(
        max_length=50, blank=True,
        help_text="যেমন: AJKS-2024-001",
    )

    category        = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES,
        default='other',
    )

    project_type    = models.CharField(
        max_length=20, choices=PROJECT_TYPE_CHOICES,
        default='long',
    )

    status          = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default='ongoing',
    )

    cover_image     = models.ImageField(
        upload_to='projects/covers/', blank=True, null=True,
    )

    short_description = models.TextField(
        max_length=400,
        help_text="List page-এ show হবে (max 400 chars)",
    )


    # =========================================================
    # DETAILS
    # =========================================================
    full_description = CKEditor5Field(
        'Full Description',
        config_name='default',
        blank=True,
    )

    objective        = models.TextField(blank=True)
    goal             = models.TextField(blank=True)


    # =========================================================
    # DATES
    # =========================================================
    start_date       = models.DateField(blank=True, null=True)
    end_date         = models.DateField(blank=True, null=True)
    duration         = models.CharField(
        max_length=100, blank=True,
        help_text="যেমন: 24 months",
    )


    # =========================================================
    # LOCATION & BENEFICIARIES
    # =========================================================
    location         = models.CharField(max_length=250, blank=True)
    implementing_area = models.CharField(max_length=250, blank=True)
    target_beneficiaries = models.CharField(max_length=250, blank=True)
    beneficiary_count    = models.PositiveIntegerField(default=0)


    # =========================================================
    # PARTNERS
    # =========================================================
    donor_partner       = models.CharField(max_length=250, blank=True)
    project_manager     = models.CharField(max_length=200, blank=True)


    # =========================================================
    # BUDGET
    # =========================================================
    total_budget             = models.DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    donor_contribution       = models.DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    organization_contribution = models.DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    other_funding            = models.DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    budget_details           = CKEditor5Field(
        'Budget Details',
        config_name='default',
        blank=True,
    )
    financial_progress       = models.PositiveIntegerField(
        default=0, help_text="0 — 100 (%)",
    )


    # =========================================================
    # PROGRESS
    # =========================================================
    overall_progress    = models.PositiveIntegerField(
        default=0, help_text="0 — 100 (%)",
    )
    physical_progress   = models.PositiveIntegerField(
        default=0, help_text="0 — 100 (%)",
    )
    completed_activities = CKEditor5Field(
        'Completed Activities',
        config_name='default',
        blank=True,
    )
    ongoing_activities   = CKEditor5Field(
        'Ongoing Activities',
        config_name='default',
        blank=True,
    )
    upcoming_activities  = CKEditor5Field(
        'Upcoming Activities',
        config_name='default',
        blank=True,
    )
    key_achievements     = CKEditor5Field(
        'Key Achievements',
        config_name='default',
        blank=True,
    )
    challenges           = CKEditor5Field(
        'Challenges',
        config_name='default',
        blank=True,
    )
    solutions            = CKEditor5Field(
        'Solutions / Mitigation',
        config_name='default',
        blank=True,
    )


    # =========================================================
    # OUTCOME (Completed projects)
    # =========================================================
    achievements        = CKEditor5Field(
        'Achievements',
        config_name='default',
        blank=True,
    )
    outcome_impact      = CKEditor5Field(
        'Outcome / Impact',
        config_name='default',
        blank=True,
    )
    success_story       = CKEditor5Field(
        'Success Story',
        config_name='default',
        blank=True,
    )
    final_report_pdf    = models.FileField(
        upload_to='projects/reports/', blank=True, null=True,
    )
    evaluation_report_pdf = models.FileField(
        upload_to='projects/reports/', blank=True, null=True,
    )


    # =========================================================
    # META
    # =========================================================
    is_active   = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="ছোট number আগে দেখাবে",
    )
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.project_name) or 'project'
            slug = base
            i = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)


# =========================================================
# GALLERY
# =========================================================
class ProjectGallery(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='gallery',
    )
    image   = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=250, blank=True)
    photo_date = models.DateField(blank=True, null=True)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return f"Gallery — {self.project.project_name}"


# =========================================================
# DOCUMENTS
# =========================================================
class ProjectDocument(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='documents',
    )
    title = models.CharField(max_length=200)
    file  = models.FileField(upload_to='projects/documents/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Project Document'
        verbose_name_plural = 'Project Documents'

    def __str__(self):
        return self.title


# =========================================================
# UPDATES
# =========================================================
class ProjectUpdate(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='updates',
    )
    title = models.CharField(max_length=200)
    content = CKEditor5Field(
        'Content',
        config_name='default',
        blank=True,
    )
    date  = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Project Update'
        verbose_name_plural = 'Project Updates'

    def __str__(self):
        return self.title


# =========================================================
# VIDEO
# =========================================================
class ProjectVideo(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='videos',
    )
    title      = models.CharField(max_length=200, blank=True)
    youtube_url = models.URLField(
        help_text="YouTube video link",
    )

    class Meta:
        verbose_name = 'Project Video'
        verbose_name_plural = 'Project Videos'

    def __str__(self):
        return self.title or self.youtube_url
    
    
# =========================================================
#  EXTERNAL LINKS
# =========================================================
class ProjectLink(models.Model):

    LINK_TYPE_CHOICES = [
        ('website',    'Official Website'),
        ('report',     'Report / Document'),
        ('donate',     'Donation Page'),
        ('facebook',   'Facebook Page'),
        ('youtube',    'YouTube Channel'),
        ('news',       'News Article'),
        ('portal',     'Project Portal'),
        ('other',      'Other'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='links',
    )

    title = models.CharField(
        max_length=200,
        help_text="যেমন: Project Official Website",
    )

    url = models.URLField(
        help_text="Full URL (https:// সহ)",
    )

    link_type = models.CharField(
        max_length=20,
        choices=LINK_TYPE_CHOICES,
        default='website',
    )

    description = models.CharField(
        max_length=300,
        blank=True,
        help_text="Optional short description",
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', 'id']
        verbose_name        = 'Project Link'
        verbose_name_plural = 'Project Links'

    def __str__(self):
        return f"{self.title} — {self.project.project_name}"

    def get_icon(self):
        """প্রতিটা link_type-এর জন্য icon class return করে"""
        icons = {
            'website':  'bi-globe2',
            'report':   'bi-file-earmark-text',
            'donate':   'bi-heart-fill',
            'facebook': 'bi-facebook',
            'youtube':  'bi-youtube',
            'news':     'bi-newspaper',
            'portal':   'bi-box-arrow-up-right',
            'other':    'bi-link-45deg',
        }
        return icons.get(self.link_type, 'bi-link-45deg')

    def get_color(self):
        """প্রতিটা type-এর জন্য color"""
        colors = {
            'website':  '#075447',
            'report':   '#1467c4',
            'donate':   '#c93030',
            'facebook': '#1877f2',
            'youtube':  '#ff0000',
            'news':     '#d18d00',
            'portal':   '#0b8a6f',
            'other':    '#666',
        }
        return colors.get(self.link_type, '#666')