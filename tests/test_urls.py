from http import HTTPStatus
from django.test import TestCase, Client

from quiz.models import Quiz
from users.models import User

OK = HTTPStatus.OK
FOUND = HTTPStatus.FOUND
NOT_FOUND = HTTPStatus.NOT_FOUND


class TaskURLTests(TestCase):
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
        self.guest_client = Client()
        self.user = User.objects.create_user(username="HasNoName")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            "quiz/index.html": "/",
            "users/index.html": "/auth/userlist/",
            "users/profile.html": "/auth/profile/",
            "users/logged_out.html": "/auth/logout/",
            "core/404.html": "/notexisted/",
        }
        for template, address in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_home_url_uses_correct_template_for_guest_client(self):
        """Страница по адресу / использует шаблон quiz/greeting.html для анонима."""
        response = self.guest_client.get("/")
        self.assertTemplateUsed(response, "quiz/greeting.html")

    def test_home_url_uses_correct_answer_for_guest_client(self):
        """URL-адресы показывают анонимного пользователя правильные ошибки."""
        url_codes_names = {
            "/": OK,
            "/auth/logout/": OK,
            "/auth/login/": OK,
            "/auth/signup/": OK,
            "/auth/userlist/": FOUND,
            "/auth/profile/": FOUND,
            "/notexisted/": NOT_FOUND,
        }
        for address, code in url_codes_names.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, code)
