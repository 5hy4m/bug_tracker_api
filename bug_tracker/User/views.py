from django.contrib.auth.models import User
from bug_tracker.models import Board,User_Activity
from rest_framework import viewsets
from bug_tracker.User.serializers import UserSerializer,UserActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = User_Activity.objects.all()
    serializer_class = UserActivitySerializer