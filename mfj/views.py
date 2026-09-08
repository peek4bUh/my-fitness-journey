from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Exercise


def workouts_index(request):
    template = loader.get_template("workouts/index.html")
    return HttpResponse(template.render(request=request))


def exercises_index(request):
    ejercicios = Exercise.objects.all().order_by(
        'name')  # Ordenados alfabéticamente
    # Si quieres limitar la cantidad:
    # ejercicios = Exercise.objects.all()[:10]  # Solo los 10 primeros

    context = {
        'exercises': ejercicios,
        'total_exercises': ejercicios.count(),
    }
    return render(request, 'exercises/index.html', context)
