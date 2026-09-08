from django.http import HttpResponse
from django.template import loader


def workouts_index(request):
    template = loader.get_template("workouts/index.html")
    return HttpResponse(template.render(request=request))


def exercises_index(request):
    template = loader.get_template("exercises/index.html")
    return HttpResponse(template.render(request=request))
