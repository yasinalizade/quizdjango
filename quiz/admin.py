from django.contrib import admin

from .models import Quiz, PassedQuiz


@admin.register(Quiz)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )
    list_filter = ('question',)
    empty_value_display = '--пусто--'


@admin.register(PassedQuiz)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'quiz',
    )
    list_filter = ('user', 'quiz')
    empty_value_display = '--пусто--'
