from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    """Пользовательская модель пользователя."""

    username = models.CharField(
        _("Имя пользователя"),
        max_length=150,
        unique=True
    )
    password = models.CharField(_("Пароль"), max_length=250)
    first_name = models.CharField(_("Имя"), max_length=150)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    email = models.EmailField(_("E-mail"), max_length=254, unique=True)
    scores = models.PositiveSmallIntegerField(_("Очки"), default=0)

    class Meta:
        ordering = ("-pk",)
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name
