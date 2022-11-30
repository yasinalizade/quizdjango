from django.db import models
from django.utils.translation import gettext as _


class QuizModel(models.Model):
    question = models.CharField(_("Вопрос"), max_length=200, null=True)
    op1 = models.CharField(_("Вариант 1"), max_length=200, null=True)
    op2 = models.CharField(_("Вариант 2"), max_length=200, null=True)
    op3 = models.CharField(_("Вариант 3"), max_length=200, null=True)
    op4 = models.CharField(_("Вариант 4"), max_length=200, null=True)
    answer = models.CharField(_("Ответ"), max_length=200, null=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = _("Тест")
        verbose_name_plural = _("Тесты")

    def __str__(self):
        return self.question
