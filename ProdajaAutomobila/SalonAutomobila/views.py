from django.shortcuts import render, get_object_or_404
from .models import Segment, Automobil
from KorpaZaKupovinu.korpa import Korpa
from KorpaZaKupovinu.forms import FormaZaDodavanjeAutomobilaUKorpu


def ListaAutomobila(request, segment_slug=None): # vraca katalog kao html
    segment = None
    segmenti = Segment.objects.all()
    automobili = Automobil.objects.filter(raspoloziv=True)
    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        automobili = automobili.filter(segment=segment)
    korpa = Korpa(request)
    return render(request, 'SalonAutomobila/automobil/list.html',
{'segment': segment, 'segmenti': segmenti,
'automobili': automobili, 'korpa':korpa})
# vraćanje podatka o jednom automobilu prema prosleđenom id automobila:
def DetaljiAutomobila(request, id, slug):
# vraca podatke o automobilu za dati id i slug kao html odgovor
    automobil = get_object_or_404(Automobil, id=id, slug=slug,
    raspoloziv=True)
    korpa = Korpa(request)
    formazadodavanjeautomobilaukorpu = FormaZaDodavanjeAutomobilaUKorpu()
    return render(request, 'SalonAutomobila/automobil/detail.html',{'automobil': automobil,  'formazadodavanjeautomobilaukorpu': formazadodavanjeautomobilaukorpu, 'korpa':korpa
})