from django.shortcuts import render
from KorpaZaKupovinu.korpa import Korpa
from .models import StavkaPorudzbine
from .forms import FormaZaPorudzbinu

def KreiranjePorudzbine(request):
    korpa = Korpa(request)
    if request.method == 'POST':
        forma = FormaZaPorudzbinu(request.POST)
        if forma.is_valid():
            porudzbina = forma.save()
            for stavka in korpa:
                StavkaPorudzbine.objects.create(porudzbina=porudzbina,
                    automobil=stavka['automobil'], cena=stavka['cena'],
                    kolicina=stavka['kolicina'])
            korpa.ObrisiJeIzSesije()
# npr. mogla bi se porudzbina smestiti i u pfd fajl
            return render(request, 'Porudzbina//created.html',
                        {'porudzbina': porudzbina})
    else:
        forma = FormaZaPorudzbinu()
    return render(request, 'Porudzbina//create.html',
        {'korpa': korpa, 'forma': forma})
