from django.test import TestCase
from quiz.models import Quiz


class QuizModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.quiz = Quiz.objects.create(
            question="В чем смысл жизни",
            op1="1",
            op2="2",
            op3="Нет ответа",
            op4="42",
            answer=4,
        )

    def test_title_label(self):
        """verbose_name совпадает с ожидаемым."""
        quiz = QuizModelTest.quiz
        field_verboses = {
            "question": "Вопрос",
            "op1": "Вариант 1",
            "op2": "Вариант 2",
            "op3": "Вариант 3",
            "op4": "Вариант 4",
            "answer": "Ответ",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    quiz._meta.get_field(field).verbose_name, expected_value
                )

    def test_title_help_text(self):
        """help_text совпадает с ожидаемым."""
        quiz = QuizModelTest.quiz
        field_help_texts = {
            "question": "Указывайте без знака вопрос",
            "answer": "Выберите номер варианта",
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    quiz._meta.get_field(field).help_text, expected_value
                )

    def test_object_name_is_title_field(self):
        """__str__  quistion - это строчка с содержимым quiz.question."""
        quiz = QuizModelTest.quiz
        expected_object_name = quiz.question
        self.assertEqual(expected_object_name, str(quiz))
