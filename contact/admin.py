from django.contrib import admin
from django.utils.html import format_html

from .models import ContactMessage
from .utils import generate_contact_pdf


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display  = (
        'id', 'name', 'phone', 'email',
        'subject_display', 'short_message',
        'is_read', 'created_at', 'pdf_link'
    )
    list_filter   = ('subject', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at', 'pdf_link_detail')

    list_per_page = 20

    fieldsets = (
        ('Sender Info', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Admin', {
            'fields': ('is_read', 'created_at', 'pdf_link_detail')
        }),
    )


    # ---------- Custom columns ----------

    def subject_display(self, obj):
        return obj.get_subject_display()
    subject_display.short_description = 'Subject'


    def short_message(self, obj):
        text = obj.message[:45] + ('...' if len(obj.message) > 45 else '')
        return text
    short_message.short_description = 'Message'


    def pdf_link(self, obj):
        url = f"/media/contact_pdfs/message_{obj.id}.pdf"
        return format_html(
            '<a href="{}" target="_blank" '
            'style="background:#075447;color:#fff;padding:4px 10px;'
            'border-radius:4px;text-decoration:none;font-size:12px;">'
            '📄 PDF</a>',
            url
        )
    pdf_link.short_description = 'PDF'


    def pdf_link_detail(self, obj):
        url = f"/media/contact_pdfs/message_{obj.id}.pdf"
        return format_html(
            '<a href="{}" target="_blank">Download PDF</a>',
            url
        )
    pdf_link_detail.short_description = 'PDF Report'


    # ---------- Auto PDF on save ----------

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        try:
            generate_contact_pdf(obj)
        except Exception as e:
            # Admin panel-এ error দেখাবে না, শুধু log হবে
            print(f"[PDF ERROR] {e}")