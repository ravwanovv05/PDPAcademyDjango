from django.db import models
from users.models import TelegramUser


class Thing(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    responsible_user = models.ForeignKey(TelegramUser, verbose_name="Responsible user", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Thing'
        verbose_name_plural = 'Things'

    def __str__(self):
        return self.name

