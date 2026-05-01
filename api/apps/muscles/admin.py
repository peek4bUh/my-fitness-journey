from django.contrib import admin

from apps.muscles.models import Muscle


class MuscleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "original",
        "english",
        "created_at",
    )


admin.site.register(Muscle, MuscleAdmin)
