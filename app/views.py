from django.shortcuts import render, redirect
from .models import Profile,Projects,Skills
from django.core.mail import send_mail

def home(request):
    profiles = Profile.objects.all()
    projects = Projects.objects.all()
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

        send_mail(
            subject=f"message from {email} by {name}", 
            message=message,
            from_email='connect@roshandamor.site',
            recipient_list=['a78778206@gmail.com'],
            fail_silently=False,
        )
        context = {
        'profiles': profiles,
        'projects': projects,
        'skills': skills,
        'success': True,
        }
    return render(request, 'home.html', context)
