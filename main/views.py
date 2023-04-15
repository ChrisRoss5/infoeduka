import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Kolegij, Obavijest
from .forms import ObavijestForm, KolegijForm, PredavacForm


def obavijesti(request):
    obavijesti = Obavijest.objects.filter(
        datum_isteka__gte=datetime.datetime.now()
    ).order_by("-datum_objave")
    return render(request, "main/obavijesti.html", {"obavijesti": obavijesti})


def obavijesti_nova(request):
    if request.method == "POST":
        form = ObavijestForm(data=request.POST)
        if form.is_valid():
            obavijest = form.save(commit=False)
            obavijest.autor = request.user
            obavijest.save()
            return redirect("/obavijesti")
    else:
        form = ObavijestForm(user=request.user)
    return render(request, "main/forma.html", {"form": form})


def predavaci_novi(request):
    if request.method == "POST":
        form = PredavacForm(request.POST)
        if form.is_valid():
            predavac = form.save(commit=False)
            predavac.username = form.cleaned_data["email"]
            predavac.set_password(form.cleaned_data["password"])
            predavac.save()
            return redirect("/predavaci")
    else:
        form = PredavacForm()
    return render(request, "main/forma.html", {"form": form})


def kolegij_novi(request):
    if request.method == "POST":
        form = KolegijForm(request.POST)
        if form.is_valid():
            kolegij = form.save(commit=False)
            kolegij.save()
            return redirect("/kolegiji")
    else:
        form = KolegijForm()
    return render(request, "main/forma.html", {"form": form})


def uredi_obavijest(request, id):
    try:
        data = Obavijest.objects.get(id=id)
        if request.method == "POST":
            form = ObavijestForm(data=request.POST)
            if form.is_valid():
                data.kolegij = form.cleaned_data["kolegij"]
                data.naziv = form.cleaned_data["naziv"]
                data.opis = form.cleaned_data["opis"]
                data.datum_isteka = form.cleaned_data["datum_isteka"]
                data.save()
                return redirect("/obavijesti")
        else:
            form = ObavijestForm(instance=data, user=request.user)
        return render(request, "main/forma.html", {"form": form})
    except Exception as e:
        print(e)


def uredi_kolegij(request, id):
    try:
        data = Kolegij.objects.get(id=id)
        if request.method == "POST":
            form = KolegijForm(request.POST)
            if form.is_valid():
                data.predavaci.set(form.cleaned_data["predavaci"])
                data.naziv = form.cleaned_data["naziv"]
                data.save()
                return redirect("/kolegiji")
        else:
            form = KolegijForm(instance=data)
        return render(request, "main/forma.html", {"form": form})
    except Exception as e:
        print(e)


def uredi_predavaca(request, id):
    data = User.objects.get(id=id)
    if request.method == "POST":
        form = PredavacForm(request.POST)
        if form.is_valid():
            data.first_name: form.cleaned_data["first_name"]
            data.last_name: form.cleaned_data["last_name"]
            data.username: form.cleaned_data["email"]
            data.email: form.cleaned_data["email"]
            data.set_password(form.cleaned_data["password"])
            data.save()
            return redirect("/predavaci")
    else:
        data.password = ""
        form = PredavacForm(instance=data)
    return render(request, "main/forma.html", {"form": form})


def kolegiji(request):
    kolegiji = (
        Kolegij.objects.filter(predavaci=request.user)
        if not request.user.is_staff
        else Kolegij.objects.all()
    )
    return render(request, "main/kolegiji.html", {"kolegiji": kolegiji})


def predavaci(request):
    predavaci = User.objects.filter(is_staff=False)
    return render(request, "main/predavaci.html", {"predavaci": predavaci})


def obrisi_obavijest(request, id):
    Obavijest.objects.get(id=id).delete()
    return redirect("/obavijesti")


def obrisi_kolegij(request, id):
    Kolegij.objects.get(id=id).delete()
    return redirect("/kolegiji")


def obrisi_predavaca(request, id):
    User.objects.get(id=id).delete()
    return redirect("/predavaci")
