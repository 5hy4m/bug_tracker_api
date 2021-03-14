from rest_framework import routers, serializers, viewsets
from bug_tracker.User.views import UserViewSet
from bug_tracker.Board.views import BoardViewSet
from bug_tracker.List.views import ListViewSet
from bug_tracker.Card.views import CardViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'board', BoardViewSet)
router.register(r'list', ListViewSet)
router.register(r'card', CardViewSet)