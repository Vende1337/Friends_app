from django.contrib.auth.models import User
from rest_framework import serializers

from friend.models import FriendRequest, Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

  
    

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(default=serializers.CurrentUserDefault())
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ('id', 'from_user', 'to_user')    


class FriendshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    friend = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ('id', 'user', 'friend')