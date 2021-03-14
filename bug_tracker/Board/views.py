from bug_tracker.models import Board
from rest_framework import viewsets
from bug_tracker.Board.serializers import BoardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer