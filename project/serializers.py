from rest_framework.serializers import ModelSerializer

from project.models import Project, Customer, Address, Birq

from drf_writable_nested.serializers import WritableNestedModelSerializer

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class BirqSerializer(ModelSerializer):
    class Meta:
        model = Birq
        fields = "__all__"

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ProjectOutSerializer(ModelSerializer):
    birq = BirqSerializer(many=True)
    customer = CustomerSerializer()
    address = AddressSerializer()

    class Meta:
        model = Project
        fields = "__all__"

class ProjectInSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'