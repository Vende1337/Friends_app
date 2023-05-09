from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet,
    FriendshipViewSet,
    FriendRequestViewSet,
)


router_v1 = routers.DefaultRouter()

router_v1.register('users', UserViewSet, basename='user-create')
router_v1.register('friends', FriendshipViewSet, basename='friends')
router_v1.register('friends/requests', FriendRequestViewSet,
                   basename='friend_requests')


urlpatterns = [
    path('api/', include(router_v1.urls)),
]
