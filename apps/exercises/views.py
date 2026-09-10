from django.shortcuts import render
from django.urls import reverse

from .models import Exercise


def exercises_index(request):
    query = request.GET.get('q', '').strip()
    exercises = Exercise.objects.select_related(
        'target_muscle', 'level').order_by('name')
    if query:
        exercises = exercises.filter(name__icontains=query)

    add_to_workout = request.GET.get('mode') == 'workout'
    workout_id = request.GET.get('workout_id')
    if add_to_workout and workout_id and workout_id.isdigit():
        return_url = reverse('workout_edit', args=[workout_id])
    else:
        return_url = reverse('workout_create')

    context = {
        'exercises': exercises,
        'query': query,
        'add_to_workout': add_to_workout,
        'return_url': return_url,
        'total_exercises': exercises.count(),
    }
    return render(request, 'exercises/list-exercise.html', context)
