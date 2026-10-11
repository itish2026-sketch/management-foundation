from django.shortcuts import render

from .models import (
    CGBChairman,
    OrganizationStructure,
    AboutAJKS,
    CGBMember,
    ChairmanMessage,
    ManagementTeam,
    ManagementPerson,
)


def about_ajks(request):

    about_list = (
        AboutAJKS.objects
        .filter(
            category="about",
            is_active=True
        )
        .order_by("display_order", "created_at")
    )

    return render(
        request,
        "about_us/about_ajks.html",
        {
            "about_list": about_list
        }
    )


def our_team(request):

    team_list = (
        AboutAJKS.objects
        .filter(
            category="team",
            is_active=True
        )
        .order_by("display_order", "created_at")
    )

    return render(
        request,
        "about_us/our_team.html",
        {
            "team_list": team_list
        }
    )


def mission_vision(request):

    mission_vision_list = (
        AboutAJKS.objects
        .filter(
            category="mission_vision",
            is_active=True
        )
        .order_by("display_order", "created_at")
    )

    return render(
        request,
        "about_us/mission_vision.html",
        {
            "mission_vision_list": mission_vision_list
        }
    )
    
    
    
    
def organization_structure(request):

    organization_list = (
        OrganizationStructure.objects
        .filter(is_active=True)
        .order_by("display_order", "created_at")
    )

    return render(
        request,
        "about_us/organization_structure.html",
        {
            "organization_list": organization_list
        }
    )
    
    

def cgb(request):

    chairman = (
        CGBChairman.objects
        .filter(is_active=True)
        .first()
    )

    members = (
        CGBMember.objects
        .filter(is_active=True)
        .order_by(
            "display_order",
            "created_at"
        )
    )

    return render(
        request,
        "about_us/cgb.html",
        {
            "chairman": chairman,
            "members": members,
        }
    )
    
    
    
# =========================================================
# CHAIRMAN'S MESSAGE
# =========================================================

def chairman_message(request):

    chairman_messages = (
        ChairmanMessage.objects
        .filter(is_active=True)
        .order_by(
            "display_order",
            "created_at"
        )
    )

    return render(
        request,
        "about_us/chairman_message.html",
        {
            "chairman_messages": chairman_messages
        }
    )
    
    
    
# =========================================================
# MANAGEMENT TEAM
# =========================================================

def management_team(request):

    team = (
        ManagementTeam.objects
        .filter(is_active=True)
        .prefetch_related("people")
        .first()
    )

    leadership = []
    members = []

    if team:

        people = (
            team.people
            .filter(is_active=True)
            .order_by(
                "profile_type",
                "display_order",
                "created_at"
            )
        )

        leadership = people.filter(
            profile_type="leadership"
        )

        members = people.filter(
            profile_type="member"
        )

    return render(
        request,
        "about_us/management_team.html",
        {
            "team": team,
            "leadership": leadership,
            "members": members,
        }
    )