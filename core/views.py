from django.shortcuts import render


def home(request):
    return render(request, "core/home_d.html")
