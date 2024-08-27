from import_export import resources
from users.models import TelegramUser


class TelegramUserResource(resources.ModelResource):
    class Meta:
        model = TelegramUser
