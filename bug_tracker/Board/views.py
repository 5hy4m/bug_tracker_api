from bug_tracker.models import Board
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from bug_tracker.Board.serializers import BoardSerializer
class BoardViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticatedOrReadOnly)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    