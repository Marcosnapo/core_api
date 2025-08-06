from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # --- Cebo de diagnóstico ---
    def list(self, request, *args, **kwargs):
        print("--- Cebo activado: Solicitud GET recibida en el backend ---")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("--- Cebo activado: Solicitud POST recibida en el backend ---")
        return super().create(request, *args, **kwargs)
