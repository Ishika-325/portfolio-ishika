from django.shortcuts import render, redirect
from .models import Profile,Projects,Skills, Contact


def home(request):
    profiles = Profile.objects.all()
    projects = Projects.objects.all().order_by('-id')[:3]
    skills = Skills.objects.all()
   
    context = {
        'profiles': profiles,
        'projects': projects,
        'skills': skills,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        success = False

        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            success = True

       
        context = {
        'profiles': profiles,
        'projects': projects,
        'skills': skills,
        'success': success,
        }
    return render(request, 'home.html', context)


def all_projects(request):
    projects = Projects.objects.all()
    return render(request, "projects.html", {"projects": projects})


