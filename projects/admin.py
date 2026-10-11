from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import (
    Project, ProjectGallery, ProjectDocument,
    ProjectUpdate, ProjectVideo,ProjectLink,
)


# =========================================================
# INLINES
# =========================================================
class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1
    fields = ('order', 'image', 'caption', 'photo_date')


class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1
    fields = ('order', 'title', 'file')


class ProjectUpdateInline(admin.StackedInline):
    model = ProjectUpdate
    extra = 0
    fields = ('date', 'title', 'content')


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1
    fields = ('title', 'youtube_url')
    
    
class ProjectLinkInline(admin.TabularInline):
    model  = ProjectLink
    extra  = 1
    fields = ('order', 'title', 'url', 'link_type', 'description', 'is_active')
    ordering = ('order',)


# =========================================================
# ADMIN
# =========================================================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project_name',
        'project_code',
        'status_badge',
        'category_display',
        'progress_bar',
        'active_toggle',
        'display_order',
        'updated_at',
    )
    list_filter    = ('status', 'category', 'project_type', 'is_active')
    search_fields  = ('project_name', 'project_code', 'location')
    prepopulated_fields = {'slug': ('project_name',)}
    readonly_fields = ('created_at', 'updated_at', 'cover_preview')

    list_per_page = 20

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'project_name', 'slug', 'project_code',
                'category', 'project_type', 'status',
                'short_description',
            )
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Details', {
            'fields': ('full_description', 'objective', 'goal'),
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'duration'),
        }),
        ('Location & Beneficiaries', {
            'fields': (
                'location', 'implementing_area',
                'target_beneficiaries', 'beneficiary_count',
            )
        }),
        ('Partners', {
            'fields': ('donor_partner', 'project_manager'),
        }),
        ('Budget', {
            'fields': (
                'total_budget', 'donor_contribution',
                'organization_contribution', 'other_funding',
                'budget_details',
            ),
            'classes': ('collapse',),
        }),
        ('Progress', {
            'fields': (
                'overall_progress', 'physical_progress',
                'financial_progress',
                'completed_activities', 'ongoing_activities',
                'upcoming_activities', 
                'key_achievements', 'challenges', 'solutions',
            ),
            'classes': ('collapse',),
        }),
        ('Completed Outcomes', {
            'fields': (
                'achievements', 'outcome_impact',
                'success_story',
                'final_report_pdf', 'evaluation_report_pdf',
            ),
            'classes': ('collapse',),
        }),
        ('Status & Order', {
            'fields': ('is_active', 'display_order'),
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    inlines = [
        ProjectLinkInline,  
        ProjectGalleryInline,
        ProjectDocumentInline,
        ProjectUpdateInline,
        ProjectVideoInline,
    ]


    # ==================================================
    # CUSTOM COLUMNS
    # ==================================================

    def category_display(self, obj):
        return obj.get_category_display()
    category_display.short_description = 'Category'


    def status_badge(self, obj):

        colors = {
            'ongoing':   '#1a8f4a',
            'completed': '#1467c4',
            'upcoming':  '#d18d00',
            'suspended': '#c93030',
        }

        color = colors.get(obj.status, '#666')

        return mark_safe(
            f'<span style="background:{color};color:#fff;'
            f'padding:3px 12px;border-radius:20px;font-size:11px;'
            f'font-weight:700;letter-spacing:.3px;">'
            f'{obj.get_status_display()}</span>'
        )
    status_badge.short_description = 'Status'


    def progress_bar(self, obj):

        p = min(obj.overall_progress, 100)

        return mark_safe(
            f'<div style="display:flex;align-items:center;gap:8px;min-width:130px;">'
            f'<div style="flex:1;height:8px;background:#eef2f0;border-radius:5px;overflow:hidden;">'
            f'<div style="height:100%;width:{p}%;background:#075447;border-radius:5px;"></div>'
            f'</div>'
            f'<span style="font-size:11px;font-weight:700;color:#075447;">{p}%</span>'
            f'</div>'
        )
    progress_bar.short_description = 'Progress'


    def active_toggle(self, obj):
        if obj.is_active:
            return mark_safe(
                '<span style="background:#075447;color:#fff;'
                'padding:3px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">● ON</span>'
            )
        return mark_safe(
            '<span style="background:#bbb;color:#fff;'
            'padding:3px 10px;border-radius:20px;font-size:11px;'
            'font-weight:700;">● OFF</span>'
        )
    active_toggle.short_description = 'Active'


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" '
                'style="max-width:400px;border-radius:10px;'
                'border:1px solid #ddd;">',
                obj.cover_image.url,
            )
        return 'No cover image uploaded yet.'
    cover_preview.short_description = 'Preview'