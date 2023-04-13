from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def kolegiji(request):
    return render(request, "main/kolegiji.html")


@login_required(login_url="/login")
def predavaci(request):
    return render(request, "main/predavaci.html")


@login_required(login_url="/login")
def obavijesti(request):
    return render(request, "main/obavijesti.html")
