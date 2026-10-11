from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutAJKS(models.Model):

    CATEGORY_CHOICES = [
        ("about", "About AJKS"),
        ("mission_vision", "Mission & Vision"),
        ("team", "Our Team"),
        ("organization", "Organization Structure"),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="about"
    )

    title = models.CharField(
        max_length=200,
        default="About AJKS"
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        default=""
    )

    content = CKEditor5Field(
        config_name="default",
        help_text="Write the complete information here."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Smaller number will appear first."
    )

    button_text = models.CharField(
        max_length=100,
        default="Back"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "About Us Information"
        verbose_name_plural = "About Us Information"
        ordering = ["category", "display_order", "created_at"]

    def __str__(self):
        return self.title
    
    
    
class OrganizationStructure(models.Model):

    title = models.CharField(
        max_length=200,
        help_text="Organization level or department name."
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        help_text="Short subtitle."
    )

    designation = models.CharField(
        max_length=200,
        blank=True,
        help_text="Designation / Position."
    )

    person_name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Person name, if applicable."
    )

    department = models.CharField(
        max_length=200,
        blank=True,
        help_text="Department / Unit name."
    )

    photo = models.ImageField(
        upload_to="organization/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    description = CKEditor5Field(
        config_name="default",
        blank=True,
        help_text="Write detailed information here."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Smaller number will appear first."
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Organization Structure"
        verbose_name_plural = "Organization Structure"
        ordering = ["display_order", "created_at"]

    def __str__(self):
        if self.person_name:
            return f"{self.person_name} - {self.designation}"
        return self.title
    
    
    
    
    
class CGBChairman(models.Model):
    title = models.CharField(
        max_length=200,
        default="Chairman",
        help_text="Chairman profile title."
    )

    name = models.CharField(
        max_length=200,
        help_text="Chairman's full name."
    )

    photo = models.ImageField(
        upload_to="cgb/chairman/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    facebook = models.URLField(
        blank=True
    )

    whatsapp = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    description = CKEditor5Field(
        config_name="default",
        blank=True,
        help_text="Chairman's detailed information. Leave blank if not needed."
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "CGB Chairman"
        verbose_name_plural = "CGB Chairman"

    def __str__(self):
        return self.name


class CGBMember(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Member designation/title."
    )

    name = models.CharField(
        max_length=200,
        help_text="Member full name."
    )

    photo = models.ImageField(
        upload_to="cgb/members/",
        blank=True,
        null=True
    )

    designation = models.CharField(
        max_length=200,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    facebook = models.URLField(
        blank=True
    )

    whatsapp = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    description = CKEditor5Field(
        config_name="default",
        blank=True,
        help_text="Detailed member information. Leave blank if not needed."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Member number/order. Smaller number appears first."
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "CGB Member"
        verbose_name_plural = "CGB Members"
        ordering = ["display_order", "created_at"]

    def __str__(self):
        return self.name
    
    
    
    
# =========================================================
# CHAIRMAN'S MESSAGE
# =========================================================

class ChairmanMessage(models.Model):

    title = models.CharField(
        max_length=250,
        default="Chairman's Message"
    )

    subtitle = models.CharField(
        max_length=350,
        blank=True,
        help_text="Optional subtitle."
    )

    message = CKEditor5Field(
        config_name="default",
        help_text="Write the Chairman's message here."
    )

    pdf_file = models.FileField(
        upload_to="chairman_messages/",
        blank=True,
        null=True,
        help_text="Optional PDF document of the Chairman's Message."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Smaller number appears first."
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Chairman's Message"
        verbose_name_plural = "Chairman's Messages"
        ordering = ["display_order", "created_at"]

    def __str__(self):
        return self.title
    
    
    
# =========================================================
# MANAGEMENT TEAM
# =========================================================

class ManagementTeam(models.Model):

    # =====================================================
    # BASIC PAGE INFORMATION
    # =====================================================

    title = models.CharField(
        max_length=250,
        default="Management Team"
    )

    subtitle = models.CharField(
        max_length=350,
        blank=True
    )

    # =====================================================
    # COVER PHOTO
    # =====================================================

    cover_photo = models.ImageField(
        upload_to="management_team/",
        blank=True,
        null=True,
        help_text="Optional cover/banner photo for Management Team."
    )

    # =====================================================
    # INTRODUCTION
    # =====================================================

    introduction = CKEditor5Field(
        config_name="default",
        blank=True,
        help_text="Optional introduction about the Management Team."
    )

    # =====================================================
    # MANAGEMENT STRUCTURE
    # =====================================================

    structure_title = models.CharField(
        max_length=250,
        blank=True,
        help_text="Title displayed before the Management Structure image."
    )

    structure_image = models.ImageField(
        upload_to="management_team/structure/",
        blank=True,
        null=True,
        help_text="Upload the full Management Team structure image."
    )

    structure_description = CKEditor5Field(
        config_name="default",
        blank=True,
        help_text="Description displayed after the Management Structure image."
    )

    # =====================================================
    # PDF DOCUMENT
    # =====================================================

    pdf_title = models.CharField(
        max_length=250,
        blank=True,
        help_text="Title displayed above the PDF reader."
    )

    pdf_file = models.FileField(
        upload_to="management_team/pdf/",
        blank=True,
        null=True,
        help_text="Upload the Management Team PDF document."
    )

    # =====================================================
    # STATUS
    # =====================================================

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Management Team Page"
        verbose_name_plural = "Management Team Page"

    def __str__(self):
        return self.title


class ManagementPerson(models.Model):

    TYPE_CHOICES = [
        ("leadership", "Leadership"),
        ("member", "Team Member"),
    ]

    team = models.ForeignKey(
        ManagementTeam,
        on_delete=models.CASCADE,
        related_name="people"
    )

    profile_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="member"
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional title."
    )

    name = models.CharField(
        max_length=200
    )

    designation = models.CharField(
        max_length=200,
        blank=True
    )

    photo = models.ImageField(
        upload_to="management_team/people/",
        blank=True,
        null=True
    )

    short_bio = models.CharField(
        max_length=500,
        blank=True
    )

    description = CKEditor5Field(
        config_name="default",
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    facebook = models.URLField(
        blank=True
    )

    whatsapp = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Management Profile"
        verbose_name_plural = "Management Profiles"
        ordering = [
            "profile_type",
            "display_order",
            "created_at"
        ]

    def __str__(self):
        return self.name