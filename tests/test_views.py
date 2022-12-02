from django.test import Client, TestCase
from django.urls import reverse

from quiz.models import Quiz
from users.models import User


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Quiz.objects.create(
            question="В чем смысл жизни",
            op1="1",
            op2="2",
            op3="Нет ответа",
            op4="42",
            answer=4,
        )

    def setUp(self):
        self.user = User.objects.create_user(username="StasBasov")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_pages_names = {
            "quiz/index.html": reverse("quiz:index"),
            "users/index.html": reverse("users:index"),
            "users/profile.html": reverse("users:profile"),
        }
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
