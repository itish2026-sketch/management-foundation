from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import WhatWeDo, WhatWeDoBlock


# ---------------- Inline Block ----------------

class WhatWeDoBlockInline(admin.StackedInline):
    model  = WhatWeDoBlock
    extra  = 1
    fields = ('order', 'text', 'image')
    ordering = ('order',)

    verbose_name        = 'Content Block'
    verbose_name_plural = 'Content Blocks  (Text → Image → Text → Image)'

    def get_extra(self, request, obj=None, **kwargs):
        # নতুন post-এ ৩টা block দিয়ে শুরু
        if obj is None:
            return 3
        return 1


# ---------------- Main Admin ----------------

@admin.register(WhatWeDo)
class WhatWeDoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'category_display',
        'active_badge',
        'blocks_count',
        'cover_thumb',
        'created_at',
    )
    list_filter   = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'cover_preview')

    list_per_page = 20

    fieldsets = (
        ('Basic Info', {
            'fields': (
                'title', 'slug',
                'category',
                'short_description',
            )
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_preview'),
        }),
        ('Status', {
            'fields': ('is_active',),
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    inlines = [WhatWeDoBlockInline]


    # -------- Custom columns --------

    def category_display(self, obj):
        return obj.get_category_display()
    category_display.short_description = 'Category'


    def active_badge(self, obj):
        if obj.is_active:
            return mark_safe(
                '<span style="background:#075447;color:#fff;'
                'padding:3px 10px;border-radius:20px;font-size:11px;'
                'font-weight:600;">● ACTIVE</span>'
            )
        return mark_safe(
            '<span style="background:#bbb;color:#fff;'
            'padding:3px 10px;border-radius:20px;font-size:11px;'
            'font-weight:600;">● INACTIVE</span>'
        )
    active_badge.short_description = 'Status'


    def blocks_count(self, obj):
        return obj.blocks.count()
    blocks_count.short_description = 'Blocks'


    def cover_thumb(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" '
                'style="width:60px;height:40px;object-fit:cover;'
                'border-radius:5px;border:1px solid #ddd;">',
                obj.cover_image.url
            )
        return '—'
    cover_thumb.short_description = 'Cover'


    def cover_preview(self, obj):
        if obj.cover_image:
            return mark_safe(
                f'<img src="{obj.cover_image.url}" '
                f'style="max-width:400px;border-radius:10px;'
                f'border:1px solid #ddd;">'
            )
        return 'No cover image uploaded yet.'
    cover_preview.short_description = 'Preview'