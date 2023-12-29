from .models import Work
from .serializers import WorkSerializer
from rest_framework import viewsets

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
