from rest_framework.viewsets import ModelViewSet

from material.models import Material
from material.serializer import MaterialSerializer

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer