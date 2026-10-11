from django.urls import path
from . import views

app_name = 'partnership'

urlpatterns = [
    path('', views.partnership_view, name='home'),
]