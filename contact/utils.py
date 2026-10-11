import os
from io import BytesIO

from django.conf import settings
from django.utils import timezone

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)


# =========================================================
# FONT REGISTER (Bengali + English)
# =========================================================

FONT_DIR = os.path.join(settings.BASE_DIR, 'contact', 'fonts')

REGULAR_FONT_PATH = os.path.join(FONT_DIR, 'NotoSansBengali-Regular.ttf')
BOLD_FONT_PATH    = os.path.join(FONT_DIR, 'NotoSansBengali-Bold.ttf')

FONT_REGULAR = 'NotoBengali'
FONT_BOLD    = 'NotoBengali-Bold'


print("REGULAR FONT:", REGULAR_FONT_PATH)
print("EXISTS:", os.path.exists(REGULAR_FONT_PATH))
print("BOLD FONT:", BOLD_FONT_PATH)
print("EXISTS:", os.path.exists(BOLD_FONT_PATH))


try:
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, REGULAR_FONT_PATH))
    pdfmetrics.registerFont(TTFont(FONT_BOLD,    BOLD_FONT_PATH))

    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily(
        FONT_REGULAR,
        normal=FONT_REGULAR,
        bold=FONT_BOLD,
        italic=FONT_REGULAR,
        boldItalic=FONT_BOLD,
    )

    print("[FONT] Registered successfully ✔")

except Exception as e:
    print(f"[FONT REGISTER ERROR] {e}")
    FONT_REGULAR = 'Helvetica'
    FONT_BOLD    = 'Helvetica-Bold'



# =========================================================
# PDF GENERATOR
# =========================================================

def generate_contact_pdf(instance):

    folder = os.path.join(settings.MEDIA_ROOT, 'contact_pdfs')
    os.makedirs(folder, exist_ok=True)

    filename = f"message_{instance.id}.pdf"
    filepath = os.path.join(folder, filename)

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName=FONT_BOLD,
        fontSize=20,
        textColor=colors.HexColor('#075447'),
        spaceAfter=20,
        alignment=1,
        leading=28,
    )

    label_style = ParagraphStyle(
        'LabelStyle',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=11,
        textColor=colors.HexColor('#555555'),
        spaceAfter=4,
        leading=18,
    )

    value_style = ParagraphStyle(
        'ValueStyle',
        parent=styles['Normal'],
        fontName=FONT_REGULAR,
        fontSize=12,
        textColor=colors.HexColor('#111111'),
        leading=22,
        spaceAfter=14,
    )

    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontName=FONT_REGULAR,
        fontSize=9,
        textColor=colors.HexColor('#888888'),
        alignment=1,
        leading=14,
    )


    elements = []

    elements.append(Paragraph("AJKS Foundation", title_style))
    elements.append(Paragraph("Contact Message Report", title_style))
    elements.append(Spacer(1, 0.4 * cm))


    info_data = [
        ["Name:",    instance.name],
        ["Phone:",   instance.phone],
        ["Email:",   instance.email],
        ["Subject:", instance.get_subject_display()],
        ["Date:",    instance.created_at.strftime('%d %b, %Y — %I:%M %p')],
    ]

    info_table = Table(info_data, colWidths=[3.5 * cm, 12 * cm])

    info_table.setStyle(TableStyle([
        ('FONTNAME',      (0, 0), (0, -1), FONT_BOLD),
        ('FONTNAME',      (1, 0), (1, -1), FONT_REGULAR),
        ('FONTSIZE',      (0, 0), (-1, -1), 11),
        ('TEXTCOLOR',     (0, 0), (0, -1), colors.HexColor('#075447')),
        ('TEXTCOLOR',     (1, 0), (1, -1), colors.HexColor('#222222')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING',    (0, 0), (-1, -1), 8),
        ('LINEBELOW',     (0, 0), (-1, -2), 0.4, colors.HexColor('#e5e5e5')),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 0.8 * cm))


    elements.append(Paragraph("Message:", label_style))
    elements.append(Spacer(1, 0.2 * cm))

    safe_message = (
        instance.message
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )

    elements.append(Paragraph(safe_message, value_style))
    elements.append(Spacer(1, 1.2 * cm))


    elements.append(Paragraph(
        f"Generated automatically on "
        f"{timezone.now().strftime('%d %b, %Y %I:%M %p')}",
        footer_style
    ))


    doc.build(elements)

    pdf_bytes = buffer.getvalue()
    buffer.close()

    with open(filepath, 'wb') as f:
        f.write(pdf_bytes)

    return f"contact_pdfs/{filename}"