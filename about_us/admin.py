from django.contrib import admin
from .models import ( 
        AboutAJKS,OrganizationStructure, 
        CGBChairman, CGBMember,
        ChairmanMessage,
        ManagementTeam,
         ManagementPerson,
        )



@admin.register(AboutAJKS)
class AboutAJKSAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
        "content",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "About Us Information",
            {
                "fields": (
                    "category",
                    "title",
                    "subtitle",
                    "content",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                    "button_text",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )

    ordering = (
        "category",
        "display_order",
        "created_at",
    )
    
    
    
@admin.register(OrganizationStructure)
class OrganizationStructureAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "person_name",
        "designation",
        "department",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
        "department",
    )

    search_fields = (
        "title",
        "subtitle",
        "person_name",
        "designation",
        "department",
        "email",
        "phone",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Organization Information",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "department",
                )
            }
        ),

        (
            "Person Information",
            {
                "fields": (
                    "person_name",
                    "designation",
                    "photo",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Detailed Information",
            {
                "fields": (
                    "description",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )

    ordering = (
        "display_order",
        "created_at",
    )
    




@admin.register(CGBChairman)
class CGBChairmanAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "email",
        "phone",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "title",
        "email",
        "phone",
    )

    readonly_fields = (
        "updated_at",
    )

    fieldsets = (
        (
            "Chairman Profile",
            {
                "fields": (
                    "title",
                    "name",
                    "photo",
                    "description",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Social Media",
            {
                "fields": (
                    "linkedin",
                    "facebook",
                    "whatsapp",
                    "instagram",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            }
        ),
    )


@admin.register(CGBMember)
class CGBMemberAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "designation",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "title",
        "designation",
        "email",
        "phone",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Member Information",
            {
                "fields": (
                    "title",
                    "name",
                    "photo",
                    "designation",
                    "description",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Social Media",
            {
                "fields": (
                    "linkedin",
                    "facebook",
                    "whatsapp",
                    "instagram",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )

    ordering = (
        "display_order",
        "created_at",
    )
    
    
    
# =========================================================
# CHAIRMAN'S MESSAGE ADMIN
# =========================================================

@admin.register(ChairmanMessage)
class ChairmanMessageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
        "message",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Chairman's Message",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "message",
                )
            }
        ),

        (
            "Official PDF",
            {
                "fields": (
                    "pdf_file",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )

    ordering = (
        "display_order",
        "created_at",
    )
    
    
# =========================================================
# MANAGEMENT TEAM INLINE
# =========================================================

class ManagementPersonInline(admin.TabularInline):

    model = ManagementPerson

    extra = 1

    fields = (
        "profile_type",
        "name",
        "designation",
        "photo",
        "display_order",
        "is_active",
    )

    ordering = (
        "profile_type",
        "display_order",
        "created_at",
    )


# =========================================================
# MANAGEMENT TEAM ADMIN
# =========================================================

@admin.register(ManagementTeam)
class ManagementTeamAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
        "introduction",
        "structure_title",
        "structure_description",
        "pdf_title",
    )

    readonly_fields = (
        "updated_at",
    )

    fieldsets = (

        # =================================================
        # BASIC INFORMATION
        # =================================================

        (
            "Management Team Information",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "cover_photo",
                    "introduction",
                )
            }
        ),

        # =================================================
        # MANAGEMENT STRUCTURE
        # =================================================

        (
            "Management Team Structure",
            {
                "fields": (
                    "structure_title",
                    "structure_image",
                    "structure_description",
                ),
                "description": (
                    "Upload the complete Management Team structure "
                    "image. The image will be displayed in large "
                    "size on the website with zoom support."
                ),
            }
        ),

        # =================================================
        # PDF DOCUMENT
        # =================================================

        (
            "Management Team PDF Document",
            {
                "fields": (
                    "pdf_title",
                    "pdf_file",
                ),
                "description": (
                    "Upload the complete PDF document. "
                    "The PDF will be displayed in a scrollable "
                    "reader on the website."
                ),
            }
        ),

        # =================================================
        # DISPLAY SETTINGS
        # =================================================

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                )
            }
        ),

        # =================================================
        # SYSTEM INFORMATION
        # =================================================

        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            }
        ),
    )

    list_display = (
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
        "introduction",
    )

    readonly_fields = (
        "updated_at",
    )

    inlines = [
        ManagementPersonInline
    ]

    fieldsets = (

        (
            "Management Team",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "cover_photo",
                    "introduction",
                )
            }
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            }
        ),
    )
    
    
    
@admin.register(ManagementPerson)
class ManagementPersonAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "profile_type",
        "designation",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "profile_type",
        "is_active",
    )

    search_fields = (
        "name",
        "title",
        "designation",
        "email",
        "phone",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Profile",
            {
                "fields": (
                    "team",
                    "profile_type",
                    "title",
                    "name",
                    "designation",
                    "photo",
                )
            }
        ),

        (
            "Biography",
            {
                "fields": (
                    "short_bio",
                    "description",
                )
            }
        ),

        (
            "Contact",
            {
                "fields": (
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Social Media",
            {
                "fields": (
                    "linkedin",
                    "facebook",
                    "whatsapp",
                    "instagram",
                )
            }
        ),

        (
            "Display",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            }
        ),

        (
            "System",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )

    ordering = (
        "profile_type",
        "display_order",
        "created_at",
    )