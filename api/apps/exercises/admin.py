from django.contrib import admin
from .models import ExerciseLevel, Exercise, ExerciseMuscle, ExerciseForce, ExerciseMechanic, ExerciseBodyRegion, ExerciseCategory


@admin.register(ExerciseForce)
class ExerciseForceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ExerciseMechanic)
class ExerciseMechanicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ExerciseBodyRegion)
class ExerciseBodyRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ExerciseLevel)
class ExerciseLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ExerciseMuscleInline(admin.TabularInline):
    """
    Permite añadir/editar músculos secundarios y terciarios
    directamente en el formulario del ejercicio.
    """
    model = ExerciseMuscle
    extra = 0                          # No mostrar filas vacías por defecto
    fields = ['muscle', 'role']
    autocomplete_fields = ['muscle']   # Búsqueda cómoda del músculo

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('muscle')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'target_muscle', 'level']
    list_filter = ['level', 'target_muscle', 'force']
    search_fields = ['name', 'description']
    autocomplete_fields = ['target_muscle']
    inlines = [ExerciseMuscleInline]
