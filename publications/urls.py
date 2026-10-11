from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [
    # ---- Annual Reports ----
    path('reports/',                  views.report_list,        name='report_list'),
    path('reports/<slug:slug>/',      views.report_detail,      name='report_detail'),

    # ---- Publications ----
    path('',                          views.publication_list,   name='publication_list'),
    path('publications/<slug:slug>/', views.publication_detail, name='publication_detail'),

    # ---- Documents ----
    path('documents/',                views.document_list,       name='document_list'),
]