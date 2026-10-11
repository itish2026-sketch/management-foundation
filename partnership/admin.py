from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import (
    Partner, PartnershipInfo, PartnershipBenefit,
    PartnershipTimeline, PartnershipStat,
)


# =========================================================
# PARTNER ADMIN
# =========================================================
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'logo_thumb', 'name',
        'category_display', 'since_year',
        'featured_badge', 'active_badge', 'display_order',
    )
    list_filter   = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'short_description')
    readonly_fields = ('logo_preview',)

    list_per_page = 20

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category', 'since_year', 'location')
        }),
        ('Logo', {
            'fields': ('logo', 'logo_preview')
        }),
        ('Description', {
            'fields': ('short_description', 'full_description')
        }),
        ('Links', {
            'fields': ('website',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
    )


    def logo_thumb(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;'
                'object-fit:contain;background:#fff;border-radius:8px;'
                'border:1px solid #eee;padding:4px;">',
                obj.logo.url,
            )
        return '—'
    logo_thumb.short_description = 'Logo'


    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-width:200px;'
                'border-radius:10px;border:1px solid #ddd;padding:8px;'
                'background:#fff;">',
                obj.logo.url,
            )
        return 'No logo uploaded.'
    logo_preview.short_description = 'Preview'


    def category_display(self, obj):
        return obj.get_category_display()
    category_display.short_description = 'Category'


    def featured_badge(self, obj):
        if obj.is_featured:
            return mark_safe(
                '<span style="background:#d18d00;color:#fff;'
                'padding:2px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">★ FEATURED</span>'
            )
        return '—'
    featured_badge.short_description = 'Featured'


    def active_badge(self, obj):
        if obj.is_active:
            return mark_safe(
                '<span style="background:#075447;color:#fff;'
                'padding:2px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">● ON</span>'
            )
        return mark_safe(
            '<span style="background:#bbb;color:#fff;'
            'padding:2px 10px;border-radius:20px;font-size:11px;'
            'font-weight:700;">● OFF</span>'
        )
    active_badge.short_description = 'Active'


# =========================================================
# PAGE INFO (Singleton)
# =========================================================
@admin.register(PartnershipInfo)
class PartnershipInfoAdmin(admin.ModelAdmin):

    list_display = ('heading', 'sub_heading')

    fieldsets = (
        ('Page Header', {
            'fields': ('heading', 'sub_heading', 'background_image')
        }),
        ('Intro Text', {
            'fields': ('intro_text',)
        }),
    )

    def has_add_permission(self, request):
        # শুধু একটা instance allow
        return not PartnershipInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# =========================================================
# BENEFITS
# =========================================================
@admin.register(PartnershipBenefit)
class PartnershipBenefitAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter   = ('is_active',)
    search_fields = ('title',)


# =========================================================
# TIMELINE
# =========================================================
@admin.register(PartnershipTimeline)
class PartnershipTimelineAdmin(admin.ModelAdmin):

    list_display = ('id', 'year', 'title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'year')


# =========================================================
# STATS
# =========================================================
@admin.register(PartnershipStat)
class PartnershipStatAdmin(admin.ModelAdmin):

    list_display = ('id', 'value', 'label', 'icon', 'order')
    list_editable = ('order',)