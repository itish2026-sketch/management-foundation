from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import AnnualReport, Publication, Document


# =========================================================
#  ANNUAL REPORT ADMIN
# =========================================================
@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'cover_thumb', 'title',
        'year', 'featured_badge',
        'active_badge', 'display_order', 'published_at',
    )
    list_filter    = ('year', 'is_active', 'is_featured')
    search_fields  = ('title', 'year')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('cover_preview', 'updated_at')

    list_editable = ('display_order',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'year', 'summary')
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Description', {
            'fields': ('description',),
        }),
        ('PDF File', {
            'fields': ('pdf_file', 'file_size'),
        }),
        ('Status', {
            'fields': (
                'is_active', 'is_featured',
                'display_order', 'published_at',
            )
        }),
        ('Meta', {
            'fields': ('updated_at',),
            'classes': ('collapse',),
        }),
    )


    def year_display(self, obj):
        return obj.year
    year_display.short_description = 'Year'


    def featured_badge(self, obj):
        if obj.is_featured:
            return mark_safe(
                '<span style="background:#d18d00;color:#fff;'
                'padding:2px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">★</span>'
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


    def cover_thumb(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width:50px;height:60px;'
                'object-fit:cover;border-radius:5px;">',
                obj.cover_image.url,
            )
        return '—'
    cover_thumb.short_description = 'Cover'


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-width:250px;'
                'border-radius:10px;border:1px solid #ddd;">',
                obj.cover_image.url,
            )
        return 'No cover.'
    cover_preview.short_description = 'Preview'



# =========================================================
#  PUBLICATION ADMIN
# =========================================================
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'cover_thumb', 'title',
        'category_display', 'pages',
        'featured_badge', 'active_badge',
        'display_order', 'published_at',
    )
    list_filter    = ('category', 'is_active', 'is_featured')
    search_fields  = ('title', 'summary', 'author')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('cover_preview', 'updated_at')

    list_editable = ('display_order',)

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'title', 'slug', 'category',
                'summary', 'author', 'pages',
            )
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Description', {
            'fields': ('description',),
        }),
        ('File', {
            'fields': ('pdf_file', 'file_size'),
        }),
        ('Status', {
            'fields': (
                'is_active', 'is_featured',
                'display_order', 'published_at',
            )
        }),
        ('Meta', {
            'fields': ('updated_at',),
            'classes': ('collapse',),
        }),
    )


    def category_display(self, obj):
        return obj.get_category_display()
    category_display.short_description = 'Category'


    def featured_badge(self, obj):
        if obj.is_featured:
            return mark_safe(
                '<span style="background:#d18d00;color:#fff;'
                'padding:2px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">★</span>'
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


    def cover_thumb(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width:50px;height:60px;'
                'object-fit:cover;border-radius:5px;">',
                obj.cover_image.url,
            )
        return '—'
    cover_thumb.short_description = 'Cover'


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-width:250px;'
                'border-radius:10px;border:1px solid #ddd;">',
                obj.cover_image.url,
            )
        return 'No cover.'
    cover_preview.short_description = 'Preview'



# =========================================================
#  DOCUMENT ADMIN
# =========================================================
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'title', 'category_display',
        'file_type', 'file_size',
        'active_badge', 'display_order', 'uploaded_at',
    )
    list_filter    = ('category', 'is_active')
    search_fields  = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

    list_editable = ('display_order',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'short_description')
        }),
        ('File', {
            'fields': ('file', 'file_type', 'file_size'),
        }),
        ('Status', {
            'fields': ('is_active', 'display_order'),
        }),
    )


    def category_display(self, obj):
        return obj.get_category_display()
    category_display.short_description = 'Category'


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