from django.urls import path
from users.views.telegram_users import CreateTelegramUserView, TelegramUserDetailView, \
    TelegramUserListWithoutUserRoleView

urlpatterns = [
    path('create-user', CreateTelegramUserView.as_view(), name='create_user'),
    path('tg-user-detail/<int:pk>', TelegramUserDetailView.as_view(), name='tg_user_detail'),
    path('tg-user-without-user-role', TelegramUserListWithoutUserRoleView.as_view(), name='tg_without_user_role'),
]
