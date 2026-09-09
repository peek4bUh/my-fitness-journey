from django.db import transaction
from django.shortcuts import redirect, render

from .forms import WorkoutExerciseFormSet, WorkoutForm
from .models import Workout


def workouts_index(request):
    workouts = Workout.objects.prefetch_related('exercises').all()
    return render(request, 'workouts/index.html', {'workouts': workouts})


def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        exercise_formset = WorkoutExerciseFormSet(request.POST)
        if form.is_valid() and exercise_formset.is_valid():
            with transaction.atomic():
                workout = form.save()
                exercise_formset.instance = workout
                exercise_formset.save()
            return redirect('workouts_index')
    else:
        form = WorkoutForm()
        exercise_formset = WorkoutExerciseFormSet()

    return render(request, 'workouts/new.html', {
        'form': form,
        'exercise_formset': exercise_formset,
    })
