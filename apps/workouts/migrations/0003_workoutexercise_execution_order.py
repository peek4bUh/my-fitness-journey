from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0002_workoutexercise_volume_rest"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutexercise",
            name="execution_order",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
