from django.contrib import admin
from .models import ExerciseInstruction, ExerciseLevel, Exercise, ExerciseMuscle, ExerciseForce, ExerciseMechanic, ExerciseBodyRegion, ExerciseCategory


@admin.register(ExerciseForce)
class ExerciseForceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(ExerciseMechanic)
class ExerciseMechanicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(ExerciseBodyRegion)
class ExerciseBodyRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(ExerciseLevel)
class ExerciseLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


class ExerciseInstructionInline(admin.TabularInline):
    model = ExerciseInstruction
    extra = 0
    fields = ['step', 'description']


class ExerciseMuscleInline(admin.TabularInline):
    model = ExerciseMuscle
    extra = 0
    fields = ['muscle', 'role']
    autocomplete_fields = ['muscle']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('muscle')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'target_muscle', 'level']
    list_filter = ['level', 'target_muscle', 'force']
    search_fields = ['name', 'description']
    autocomplete_fields = ['target_muscle']
    inlines = [ExerciseMuscleInline, ExerciseInstructionInline]
