from django.urls import path
from . import views


app_name = "about_us"


urlpatterns = [

    path("",views.about_ajks, name="about_ajks"),
    path("our-team/",views.our_team,name="our_team"),
    path("mission-vision/",views.mission_vision,name="mission_vision"),
    path("organization-structure/",views.organization_structure,name="organization_structure"),
    path("cgb/",views.cgb,name="cgb"),
    path("chairmans-message/",views.chairman_message,name="chairman_message"),
    path("management-team/",views.management_team,name="management_team"),

]