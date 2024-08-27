from django.db import models


class TelegramUser(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('manager', 'Manager')
    ]

    first_name = models.CharField(max_length=60, verbose_name='First name')
    last_name = models.CharField(max_length=60, null=True, blank=True, verbose_name='Last name')
    username = models.CharField(max_length=60, null=True, blank=True, verbose_name='Username')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name='Role')
    telegram_id = models.PositiveBigIntegerField(unique=True, verbose_name='Telegram ID')
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Joined at')

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'

    def __str__(self):
        return self.first_name
