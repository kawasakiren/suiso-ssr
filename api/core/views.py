from rest_framework import viewsets
from .serializers import WaterPlantsSerializer
from .models import WaterPlants

# Create your views here.
class WaterPlantsViewSet(viewsets.ModelViewSet):
	serializer_class = WaterPlantsSerializer
	queryset = WaterPlants.objects.all()
