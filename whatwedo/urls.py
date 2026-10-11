from django.urls import path
from . import views

app_name = 'whatwedo'

urlpatterns = [
    path('',              views.whatwedo_list,   name='list'),
    path('<slug:slug>/',  views.whatwedo_detail, name='detail'),
]