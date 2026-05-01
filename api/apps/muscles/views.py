from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.muscles.models import Muscle
from apps.muscles.serializers import MuscleSerializer


class MuscleList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
