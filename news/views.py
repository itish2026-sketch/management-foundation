from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import News, Event, Notice


# =========================================================
#  LIST VIEWS
# =========================================================
def news_list(request):

    news = News.objects.filter(is_active=True)

    featured = news.filter(is_featured=True).first()

    context = {
        'news':     news,
        'featured': featured,
    }

    return render(request, 'news/news_list.html', context)



def event_list(request):

    status = request.GET.get('status', '')

    events = Event.objects.filter(is_active=True)

    if status:
        events = events.filter(status=status)

    context = {
        'events':   events,
        'status':   status,
        'statuses': Event.STATUS_CHOICES,
    }

    return render(request, 'news/event_list.html', context)



def notice_list(request):

    notices = Notice.objects.filter(is_active=True)

    context = {
        'notices': notices,
    }

    return render(request, 'news/notice_list.html', context)



# =========================================================
#  DETAIL VIEWS
# =========================================================
def news_detail(request, slug):

    item = get_object_or_404(News, slug=slug, is_active=True)

    related = (
        News.objects
        .filter(is_active=True, category=item.category)
        .exclude(id=item.id)[:3]
    )

    return render(request, 'news/news_detail.html', {
        'item': item,
        'related': related,
    })



def event_detail(request, slug):

    event = get_object_or_404(Event, slug=slug, is_active=True)

    related = (
        Event.objects
        .filter(is_active=True)
        .exclude(id=event.id)[:3]
    )

    return render(request, 'news/event_detail.html', {
        'event': event,
        'related': related,
    })



def notice_detail(request, slug):

    notice = get_object_or_404(Notice, slug=slug, is_active=True)

    return render(request, 'news/notice_detail.html', {
        'notice': notice,
    })



# =========================================================
#  HOMEPAGE WIDGETS
#  (Latest 3 of each)
# =========================================================
def latest_news(request):

    latest = News.objects.filter(is_active=True)[:3]

    return render(request, 'news/_latest_news.html', {
        'latest': latest,
    })