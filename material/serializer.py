from rest_framework.serializers import ModelSerializer

from material.models import Material

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"