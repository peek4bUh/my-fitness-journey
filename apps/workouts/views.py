from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import WorkoutExerciseFormSet, WorkoutForm
from .models import Workout


def workouts_index(request):
    workouts = Workout.objects.prefetch_related('exercises').all()
    return render(request, 'workouts/list-workout.html', {'workouts': workouts})


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

    return render(request, 'workouts/create-workout.html', {
        'form': form,
        'exercise_formset': exercise_formset,
    })


def workout_edit(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)

    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        exercise_formset = WorkoutExerciseFormSet(
            request.POST, instance=workout)
        if form.is_valid() and exercise_formset.is_valid():
            with transaction.atomic():
                form.save()
                exercise_formset.save()
            return redirect('workouts_index')
    else:
        form = WorkoutForm(instance=workout)
        exercise_formset = WorkoutExerciseFormSet(instance=workout)

    return render(request, 'workouts/create-workout.html', {
        'form': form,
        'exercise_formset': exercise_formset,
        'is_edit': True,
        'workout': workout,
    })


def workout_delete(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        workout.delete()
    return redirect('workouts_index')
