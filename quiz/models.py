from django.db import models
from django.utils.translation import gettext as _
from users.models import User


class Quiz(models.Model):
    """Модель квиза."""

    question = models.CharField(
        _("Вопрос"),
        max_length=200,
        null=True,
        help_text="Указывайте без знака вопрос",
    )
    op1 = models.CharField(_("Вариант 1"), max_length=200, null=True)
    op2 = models.CharField(_("Вариант 2"), max_length=200, null=True)
    op3 = models.CharField(_("Вариант 3"), max_length=200, null=True)
    op4 = models.CharField(_("Вариант 4"), max_length=200, null=True)
    answer = models.CharField(
        _("Ответ"),
        max_length=200,
        null=True,
        help_text="Выберите номер варианта",
    )

    class Meta:
        ordering = ("-pk",)
        verbose_name = _("Тест")
        verbose_name_plural = _("Тесты")

    def __str__(self):
        return self.question


class PassedQuiz(models.Model):
    """Связующая модель для пройденных маршрутов пользователя."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-pk",)
        verbose_name = _("Пройденный тест пользователя")
        verbose_name_plural = _("Пройденные тесты пользователя")

    def __str__(self):
        return f"{self.user.username} прошел {self.quiz.id}"
