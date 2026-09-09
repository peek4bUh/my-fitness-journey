from django.shortcuts import render

from .models import Exercise


def exercises_index(request):
    exercises = Exercise.objects.all().order_by('name')

    context = {
        'exercises': exercises,
        'total_exercises': exercises.count(),
    }
    return render(request, 'exercises/list-exercise.html', context)
