from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def dummy(request):
    return render(request, 'dummy.html')

def Home_Page(request):
    return render(request, 'Home_Page.html')

def register(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf, 'pf':pf}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        
        if UFD.is_valid() and PFD.is_valid():
            UFO=UFD.save(commit=False)
            UFO.set_password(UFD.cleaned_data['password'])
            UFO.save()

            PFO=PFD.save(commit=False)
            PFO.user_profile=UFO
            PFO.save()

            send_mail('Django-User registartion', 'Thanks for registration, your registration is succusseful!', 'fordjangoproject37@gmail.com', [UFO.email],fail_silently=False)
        return HttpResponse('Your registration is succusseful!!')
    return render(request, 'register.html',d)

