from rest_framework import viewsets
from bug_tracker.models import List
from .serializers import ListSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer