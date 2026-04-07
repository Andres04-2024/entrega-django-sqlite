from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hola_mundo, RolViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)

urlpatterns = [
    path('', hola_mundo),
    path('api/', include(router.urls)),
]