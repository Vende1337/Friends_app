from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import yaml
import os

from .views import (
    UserViewSet,
    FriendshipViewSet,
     FriendRequestViewSet,
    #  FriendshipDeleteView
    SwaggerSchemaView
)
from friend_app.settings import SWAGGER_YAML_FILE



router_v1 = routers.DefaultRouter()

router_v1.register('users', UserViewSet, basename='user-create')
router_v1.register('friends', FriendshipViewSet, basename='friends')
router_v1.register('friends/requests', FriendRequestViewSet, basename='friend_requests')
# router_v1.register('friends/delete', FriendshipDeleteView, basename='friendship-delete')


urlpatterns = [
    path('api/', include(router_v1.urls)),
    # path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/docs/', schema_view.with_ui()),
    # path('api/redoc/', SwaggerSchemaView.as_view(), name='swagger-schema'),
    # path('docs/', schema_view),
    # path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    # path('api/swagger-ui/', swagger_ui_view, name='swagger-ui'),

   
]