from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Kolegij, Obavijest
from .forms import ObavijestForm


@login_required(login_url="/login")
def obavijesti(request):
    obavijesti = Obavijest.objects.all()
    return render(request, "main/obavijesti.html", {"obavijesti": obavijesti})


@login_required(login_url="/login")
def obavijesti_nova(request):
    if request.method == "POST":
        form = ObavijestForm(request.POST)
        if form.is_valid():
            obavijest = form.save(commit=False)
            obavijest.autor = request.user
            obavijest.save()
            return redirect("/obavijesti")
    else:
        form = ObavijestForm()
    return render(request, "main/obavijesti-nova.html", {"form": form})


@login_required(login_url="/login")
def kolegiji(request):
    kolegiji = Kolegij.objects.all()
    return render(request, "main/kolegiji.html", {"kolegiji": kolegiji})


@login_required(login_url="/login")
def predavaci(request):
    predavaci = User.objects.filter(is_staff=False)
    return render(request, "main/predavaci.html", {"predavaci": predavaci})
