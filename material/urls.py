from django.urls import path, include
from rest_framework.routers import SimpleRouter

from material.views import MaterialViewSet

router = SimpleRouter()
router.register("", MaterialViewSet)

urlpatterns = [
    path("", include(router.urls)),
]