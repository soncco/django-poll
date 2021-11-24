from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.models import *
from core.utils import get_client_ip


def index(request):
    ultima = Encuesta.objects.filter(activo=True).order_by('-id')[0]
    if not request.user.is_authenticated:
        ip = get_client_ip(request)
        ya_voto = Ip.objects.filter(ip=ip).count()
        if ya_voto > 0:
            return HttpResponseRedirect(reverse('core:resultados', args=[ultima.pk]))
    context = {'encuesta': ultima}

    return render(request, 'core/encuesta.html', context)


def resultados(request, id):
    encuesta = get_object_or_404(Encuesta, pk=id)

    context = {'encuesta': encuesta}
    return render(request, 'core/resultados.html', context)


def registrar(request):
    opcion = Opcion.objects.get(pk=request.POST.get('opcion'))
    opcion.votos = opcion.votos+1
    opcion.save()

    if not request.user.is_authenticated:
        ip = get_client_ip(request)
        contador_ip = Ip.objects.filter(ip=ip).count()
        if contador_ip == 0:
            nuevo_ip = Ip(encuesta=opcion.encuesta, ip=ip)
            nuevo_ip.save()

    return HttpResponseRedirect(reverse('core:resultados', args=[opcion.encuesta.pk]))
