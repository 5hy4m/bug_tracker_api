from rest_framework import viewsets
from .serializers import CardSerializer
from bug_tracker.models import Card

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer