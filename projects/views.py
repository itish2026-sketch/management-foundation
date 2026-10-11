from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Project


# =========================================================
# PROJECT LIST
# =========================================================
def project_list(request):
    """
    সব active project একসাথে, filter সহ:
    - ?status=ongoing | completed | upcoming | suspended
    - ?category=education | health | community | ...
    - ?q=keyword  (title/code/description search)
    """

    status   = request.GET.get('status', '').strip()
    category = request.GET.get('category', '').strip()
    query    = request.GET.get('q', '').strip()

    projects = Project.objects.filter(is_active=True)

    # ---- Status filter ----
    if status:
        projects = projects.filter(status=status)

    # ---- Category filter ----
    if category:
        projects = projects.filter(category=category)

    # ---- Search ----
    if query:
        projects = projects.filter(
            Q(project_name__icontains=query) |
            Q(project_code__icontains=query) |
            Q(short_description__icontains=query) |
            Q(location__icontains=query)
        )

    # ---- Counts for tab badges (optional) ----
    counts = {
        'all':       Project.objects.filter(is_active=True).count(),
        'ongoing':   Project.objects.filter(is_active=True, status='ongoing').count(),
        'completed': Project.objects.filter(is_active=True, status='completed').count(),
        'upcoming':  Project.objects.filter(is_active=True, status='upcoming').count(),
        'suspended': Project.objects.filter(is_active=True, status='suspended').count(),
    }

    context = {
        'projects':   projects,
        'status':     status,
        'category':   category,
        'query':      query,
        'statuses':   Project.STATUS_CHOICES,
        'categories': Project.CATEGORY_CHOICES,
        'counts':     counts,
    }

    return render(request, 'projects/list.html', context)



# =========================================================
# PROJECT DETAIL
# =========================================================
def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
        is_active=True,
    )

    # ---- Related projects (same category, exclude current) ----
    related = (
        Project.objects
        .filter(is_active=True, category=project.category)
        .exclude(id=project.id)
        .order_by('display_order')[:3]
    )

    # ---- Gallery (already sorted by order via Meta) ----
    gallery = project.gallery.all()

    # ---- Documents ----
    documents = project.documents.all()

    # ---- Updates ----
    updates = project.updates.all()

    # ---- Videos ----
    videos = project.videos.all()
    
    # ---- Links ----
    links     = project.links.filter(is_active=True)

    context = {
        'project':   project,
        'related':   related,
        'gallery':   gallery,
        'documents': documents,
        'updates':   updates,
        'videos':    videos,
        'links':     links,   
    }

    return render(request, 'projects/detail.html', context)