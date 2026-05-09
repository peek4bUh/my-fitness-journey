from django.contrib import admin

from apps.muscles.models import Muscle, MuscleGroup, MuscleGroupMuscle


class MuscleGroupMuscleInline(admin.TabularInline):
    """
    Permite añadir/editar músculos en el grupo muscular
    directamente en el formulario.
    """
    model = MuscleGroupMuscle
    extra = 0
    fields = ['muscle']
    autocomplete_fields = ['muscle']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('muscle')


@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'muscles_list']
    search_fields = ['name']
    ordering = ['name']
    inlines = [MuscleGroupMuscleInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('muscles')

    def muscles_list(self, obj):
        return ', '.join(obj.muscles.values_list('original', flat=True))
    muscles_list.short_description = 'muscles'


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ['id', 'original', 'english']
    search_fields = ['original', 'english']
    ordering = ['original']
