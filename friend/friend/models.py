from django.db import models
from django.contrib.auth.models import User


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend_requests_sent')
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend_requests_received')
    class Meta:
        unique_together = (('from_user', 'to_user'),)


class Friendship(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend')

    class Meta:
        unique_together = (('user', 'friend'),)
