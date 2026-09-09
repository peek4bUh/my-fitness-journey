from django.db import migrations, models


def copy_legacy_volume(apps, schema_editor):
    WorkoutExercise = apps.get_model("workouts", "WorkoutExercise")
    for exercise in WorkoutExercise.objects.all():
        volume = f"{exercise.sets}x{exercise.reps}"
        if exercise.weight is not None:
            volume += f"x{exercise.weight:g}"
        exercise.volume = volume
        exercise.save(update_fields=["volume"])


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutexercise",
            name="volume",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="workoutexercise",
            name="rest",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.RunPython(copy_legacy_volume, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="workoutexercise",
            name="volume",
            field=models.CharField(max_length=255),
        ),
        migrations.RemoveField(
            model_name="workoutexercise",
            name="sets",
        ),
        migrations.RemoveField(
            model_name="workoutexercise",
            name="reps",
        ),
        migrations.RemoveField(
            model_name="workoutexercise",
            name="weight",
        ),
    ]
