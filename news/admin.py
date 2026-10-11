from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import News, Event, Notice


# =========================================================
#  NEWS ADMIN
# =========================================================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'cover_thumb',
        'title',
        'category_display',
        'featured_badge',
        'active_badge',
        'display_order',       # ⬅️ list_editable-এর জন্য দরকার
        'published_at',
    )
    list_filter    = ('category', 'is_active', 'is_featured')
    search_fields  = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('cover_preview', 'updated_at')

    list_editable = ('display_order',)

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'title', 'slug', 'category',
                'short_description', 'author',
            )
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Content', {
            'fields': ('full_content',),
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
                '<img src="{}" style="width:60px;height:40px;'
                'object-fit:cover;border-radius:5px;">',
                obj.cover_image.url,
            )
        return '—'
    cover_thumb.short_description = 'Cover'


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-width:400px;'
                'border-radius:10px;border:1px solid #ddd;">',
                obj.cover_image.url,
            )
        return 'No image.'
    cover_preview.short_description = 'Preview'



# =========================================================
#  EVENT ADMIN
# =========================================================
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'cover_thumb',
        'title',
        'status_badge',
        'start_date',
        'venue',
        'active_badge',
        'display_order',       # ⬅️ যোগ করা হলো
    )
    list_filter    = ('status', 'is_active', 'is_featured')
    search_fields  = ('title', 'venue', 'organizer')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('cover_preview',)

    list_editable = ('display_order',)   # ⬅️ যোগ করা হলো

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'title', 'slug',
                'short_description',
            )
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Description', {
            'fields': ('full_content',),
        }),
        ('Location', {
            'fields': ('venue', 'address'),
        }),
        ('Date & Time', {
            'fields': ('start_date', 'end_date'),
        }),
        ('Organizer', {
            'fields': ('organizer', 'contact'),
        }),
        ('Status', {
            'fields': (
                'status', 'is_active', 'is_featured',
                'display_order',
            )
        }),
    )


    def status_badge(self, obj):
        colors = {
            'upcoming':  '#1467c4',
            'ongoing':   '#1a8f4a',
            'completed': '#666',
            'cancelled': '#c93030',
        }
        color = colors.get(obj.status, '#666')
        return mark_safe(
            f'<span style="background:{color};color:#fff;'
            f'padding:2px 10px;border-radius:20px;font-size:11px;'
            f'font-weight:700;">{obj.get_status_display()}</span>'
        )
    status_badge.short_description = 'Status'


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
                '<img src="{}" style="width:60px;height:40px;'
                'object-fit:cover;border-radius:5px;">',
                obj.cover_image.url,
            )
        return '—'
    cover_thumb.short_description = 'Cover'


    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-width:400px;'
                'border-radius:10px;border:1px solid #ddd;">',
                obj.cover_image.url,
            )
        return 'No image.'
    cover_preview.short_description = 'Preview'



# =========================================================
#  NOTICE ADMIN
# =========================================================
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'priority_badge',
        'pinned_badge',
        'issued_by',
        'published_at',
        'deadline',
        'active_badge',
        'display_order',       # ⬅️ list_editable-এর জন্য দরকার
    )
    list_filter    = ('priority', 'is_active', 'is_pinned')
    search_fields  = ('title', 'issued_by')
    prepopulated_fields = {'slug': ('title',)}

    list_editable = ('display_order',)

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'title', 'slug',
                'short_description',
            )
        }),
        ('Content', {
            'fields': ('full_content',),
        }),
        ('Attachment', {
            'fields': ('attachment_pdf',),
        }),
        ('Details', {
            'fields': (
                'priority', 'issued_by',
                'published_at', 'deadline',
            )
        }),
        ('Status', {
            'fields': (
                'is_active', 'is_pinned', 'display_order',
            )
        }),
    )


    def priority_badge(self, obj):
        colors = {
            'normal': '#4a5652',
            'high':   '#d18d00',
            'urgent': '#c93030',
        }
        color = colors.get(obj.priority, '#666')
        return mark_safe(
            f'<span style="background:{color};color:#fff;'
            f'padding:2px 10px;border-radius:20px;font-size:11px;'
            f'font-weight:700;">{obj.get_priority_display()}</span>'
        )
    priority_badge.short_description = 'Priority'


    def pinned_badge(self, obj):
        if obj.is_pinned:
            return mark_safe(
                '<span style="background:#075447;color:#fff;'
                'padding:2px 10px;border-radius:20px;font-size:11px;'
                'font-weight:700;">📌 PINNED</span>'
            )
        return '—'
    pinned_badge.short_description = 'Pinned'


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