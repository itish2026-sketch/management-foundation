from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # ---- List pages ----
    path('',              views.news_list,   name='news_list'),
    path('events/',       views.event_list,  name='event_list'),
    path('notices/',      views.notice_list, name='notice_list'),

    # ---- Detail pages ----
    path('news/<slug:slug>/',    views.news_detail,   name='news_detail'),
    path('event/<slug:slug>/',   views.event_detail,  name='event_detail'),
    path('notice/<slug:slug>/',  views.notice_detail, name='notice_detail'),
]