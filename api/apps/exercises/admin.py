from django.contrib import admin

from apps.exercises.models import Exercise, Difficulty


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "difficulty",
    )


class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Difficulty, DifficultyAdmin)
