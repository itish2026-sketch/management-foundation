from django.shortcuts import render, get_object_or_404
from .models import AnnualReport, Publication, Document


# =========================================================
#  ANNUAL REPORTS
# =========================================================
def report_list(request):
    reports = AnnualReport.objects.filter(is_active=True)
    featured = reports.filter(is_featured=True).first()

    return render(request, 'publications/report_list.html', {
        'reports': reports,
        'featured': featured,
    })


def report_detail(request, slug):
    report = get_object_or_404(AnnualReport, slug=slug, is_active=True)

    related = (
        AnnualReport.objects
        .filter(is_active=True)
        .exclude(id=report.id)[:3]
    )

    return render(request, 'publications/report_detail.html', {
        'report': report,
        'related': related,
    })



# =========================================================
#  PUBLICATIONS
# =========================================================
def publication_list(request):
    category = request.GET.get('category', '')

    pubs = Publication.objects.filter(is_active=True)

    if category:
        pubs = pubs.filter(category=category)

    return render(request, 'publications/publication_list.html', {
        'publications': pubs,
        'category':     category,
        'categories':   Publication.CATEGORY_CHOICES,
    })


def publication_detail(request, slug):
    pub = get_object_or_404(Publication, slug=slug, is_active=True)

    related = (
        Publication.objects
        .filter(is_active=True, category=pub.category)
        .exclude(id=pub.id)[:3]
    )

    return render(request, 'publications/publication_detail.html', {
        'pub': pub,
        'related': related,
    })



# =========================================================
#  DOCUMENTS
# =========================================================
def document_list(request):
    category = request.GET.get('category', '')

    docs = Document.objects.filter(is_active=True)

    if category:
        docs = docs.filter(category=category)

    return render(request, 'publications/document_list.html', {
        'documents':  docs,
        'category':   category,
        'categories': Document.CATEGORY_CHOICES,
    })