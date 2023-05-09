from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response






from friend.models import Friendship, FriendRequest
from .serializers import UserSerializer, FriendshipSerializer,  FriendRequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FriendshipViewSet(viewsets.ModelViewSet):
    serializer_class = FriendshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        friendships = Friendship.objects.filter(
            user=self.request.user).values_list('friend', flat=True)
        return friendships

    @action(
        detail=False,
        methods=['delete'],
        url_path='delete'
    )
    def delete_friend(self, request):
        friend = get_object_or_404(User, username=request.data.get('friend'))
        if not Friendship.objects.filter(user=self.request.user, friend=friend).exists():
            raise serializers.ValidationError(
                "Пользователь которого вы хотите удалить, нет в Вашем списке друзей!")
        Friendship.objects.filter(
            user=self.request.user, friend=friend).delete()
        Friendship.objects.filter(
            user=friend, friend=self.request.user).delete()
        return Response(f"Вы удалили пользователя {friend} из своего списка друзей!", status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['get'],
        url_path='status'
    )
    def perform_create(self, requests):
        friend = get_object_or_404(
            User, username=self.request.data.get('friend'))
        if Friendship.objects.filter(user=self.request.user, friend=friend).exists():
            return Response(f"Вы и пользователь {friend}  друзья!", status=status.HTTP_200_OK)
        if FriendRequest.objects.filter(from_user=self.request.user, to_user=friend):
            return Response(f"Пользователю {friend} отправлено Ваше приглашение в дружбу!", status=status.HTTP_200_OK)
        if FriendRequest.objects.filter(from_user=friend, to_user=self.request.user):
            return Response(f"Пользователь {friend} отправил вам приглашение в дружбу!", status=status.HTTP_200_OK)
        else:
            return Response(f"У Вас с пользователем {friend} нет ничего", status=status.HTTP_200_OK)

    def get_allowed_methods(self):
        return ['GET']


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=['post'],
        url_path='send'
    )
    def perform_create(self, requests):
        friend = get_object_or_404(
            User, username=self.request.data.get('friend'))
        if Friendship.objects.filter(user=self.request.user, friend=friend):
            raise Exception(
                "Пользователь которого вы хотите добавить, уже есть в Вашем списке друзей!")
        if FriendRequest.objects.filter(from_user=friend, to_user=self.request.user):
            Friendship.objects.create(user=self.request.user, friend=friend)
            Friendship.objects.create(user=friend, friend=self.request.user)
            FriendRequest.objects.filter(
                from_user=friend, to_user=self.request.user).delete()
            return Response("Ваш запрос на добавление в друзья принят!", status=status.HTTP_200_OK)
        FriendRequest.objects.create(
            from_user=self.request.user, to_user=friend)
        return Response("Запрос на добавления в друзья отправлен!", status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['get'],
        url_path='incoming'
    )
    def incoming_requests(self, requests):
        user = self.request.user
        friend_requests = FriendRequest.objects.filter(to_user=user)
        serializer = FriendRequestSerializer(many=True, data=friend_requests)
        serializer.is_valid()
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get'],
        url_path='outgoing'
    )
    def outgoing_requests(self, requests):
        user = self.request.user
        friend_requests = FriendRequest.objects.filter(from_user=user)
        serializer = FriendRequestSerializer(many=True, data=friend_requests)
        serializer.is_valid()
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get'],
        url_path=r'incoming/(?P<id>\d+)/accept'
    )
    def accept_incoming_request(self, requests, id=None):
        friend_requests = get_object_or_404(
            FriendRequest, pk=id)
        friend = friend_requests.from_user
        Friendship.objects.create(user=self.request.user, friend=friend)
        Friendship.objects.create(user=friend, friend=self.request.user)
        friend_requests.delete()
        return Response("Вы приняли заявку в друзья!")

    @action(
        detail=False,
        methods=['get'],
        url_path=r'incoming/(?P<id>\d+)/decline'
    )
    def decline_incoming_request(self, requests, id=None):
        friend_requests = get_object_or_404(
            FriendRequest, pk=id)
        friend_requests.delete()
        return Response("Вы отклонили заявку в друзья!")
