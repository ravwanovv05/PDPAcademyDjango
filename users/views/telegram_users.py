from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.models import TelegramUser
from users.serializers.telegram_users import TelegramUserSerializer


class CreateTelegramUserView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = TelegramUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TelegramUserDetailView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.all()

    def get(self, request, pk, *args, **kwargs):
        telegram_user = TelegramUser.objects.filter(pk=pk).first()
        serializer = self.get_serializer(telegram_user)
        return Response(serializer.data)


class TelegramUserListWithoutUserRoleView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.all()

    def get(self, request, *args, **kwargs):
        telegram_users = TelegramUser.objects.exclude(role='user')
        serializer = self.get_serializer(telegram_users, many=True)
        return Response(serializer.data)
