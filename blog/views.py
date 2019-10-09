from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Entrada, Serie
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404
from .forms import FormComentario

def lista_entradas(request):
    entradas = Entrada.objects.all().order_by("-fecha")

    paginador = Paginator(entradas, 10)

    try: 
        pagina = int(request.GET.get('pagina', '1'))
    except ValueError: 
        pagina = 1
    
    try: 
        entradas = paginador.page(pagina)
    except(InvalidPage, EmptyPage):
        entradas = paginador.page(paginador.num_pages)

    return render(request, 'blog/entradas.html', {'entradas': entradas})

def entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk = pk)
    return render(request, 'blog/entrada.html', {'entrada': entrada})

def nuevo_comentario(request, pk):
    entrada = get_object_or_404(Entrada, pk = pk)
    if request.method == "POST":
        form = FormComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit = False)
            comentario.entrada = entrada
            comentario.save()
            return redirect('entrada', entrada.pk)
    else:
        form = FormComentario()
    return render(request, 'blog/comentario.html', {'form': form})

def series_activas(request):
    series = Serie.objects.all().filter(activa = True).order_by("titulo")
    estado = "Series Activas"
    return render(request, 'series/listado.html', {'series': series, 'estado': estado})

def series_terminadas(request):
    series = Serie.objects.all().filter(activa = False).order_by("titulo")
    estado = "Series Terminadas"
    return render(request, 'series/listado.html', {'series': series, 'estado': estado})