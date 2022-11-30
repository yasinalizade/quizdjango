from django.contrib import admin

from .models import QuizModel


@admin.register(QuizModel)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )
    list_filter = ('question',)
    empty_value_display = '--пусто--'
