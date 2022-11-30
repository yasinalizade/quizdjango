from django.contrib import admin

from .models import User


@admin.register(User)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email"
    )
    list_filter = ('username',)
    empty_value_display = '--пусто--'
