from django.urls import path, include

from rest_framework.routers import SimpleRouter

from project import views

router = SimpleRouter()
router.register("", views.ProjectViewSet)
router.register("address", views.AddressViewSet)
router.register("birq", views.BirqViewSet)
router.register("customer", views.CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
