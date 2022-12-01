# Generated by Django 4.1.3 on 2022-12-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_passedquiz_quiz_delete_quizmodel_passedquiz_quiz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passedquiz',
            options={'ordering': ('-pk',), 'verbose_name': 'Пройденный тест пользователя', 'verbose_name_plural': 'Пройденные тесты пользователя'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(help_text='Указывайте без знака вопрос', max_length=200, null=True, verbose_name='Вопрос'),
        ),
    ]