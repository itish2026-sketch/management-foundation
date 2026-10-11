from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("core.urls")),
    path("about-ajks/", include("about_us.urls")),
    path('contact/', include('contact.urls')),
    path('what-we-do/', include('whatwedo.urls')),
    path('projects/', include('projects.urls')),
    path('partnership/', include('partnership.urls')),
    path('news/', include('news.urls')),
    path('publications/', include('publications.urls')),  
    
    
    
    path("ckeditor5/",include("django_ckeditor_5.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)