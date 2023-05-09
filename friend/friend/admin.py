from django.contrib import admin
from django.contrib.auth.models import User

from .models import FriendRequest, Friendship

admin.site.register(Friendship)
admin.site.register(FriendRequest)

