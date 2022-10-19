from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from project.models import Project, Customer, Address, Birq
from project.serializers import ProjectInSerializer, ProjectOutSerializer, CustomerSerializer, AddressSerializer, BirqSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectInSerializer

    # Set serializers for different actions
    def get_serializer_class(self):
        if self.action == "list":
            return ProjectOutSerializer
        elif self.action == "retrieve":
            return ProjectOutSerializer
        elif self.action == "destroy":
            return ProjectOutSerializer
        return ProjectInSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class BirqViewSet(ModelViewSet):
    queryset = Birq.objects.all()
    serializer_class = BirqSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer