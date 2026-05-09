from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from apps.muscles.models import Muscle, MuscleGroup
from apps.muscles.serializers import MuscleSerializer, MuscleGroupSerializer


@extend_schema(tags=["Muscles"])
class MuscleList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer


@extend_schema(tags=["Muscles"])
class MuscleDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer


@extend_schema(tags=["Muscle Groups"])
class MuscleGroupList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


@extend_schema(tags=["Muscle Groups"])
class MuscleGroupDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer
