from django.contrib import admin
from .models import IngredientCategory, Ingredient, RecipeCategory, Recipe, RecipeIngredient

# 1. Простые модели регистрируем в одну строчку
admin.site.register(IngredientCategory)
admin.site.register(RecipeCategory)
admin.site.register(Ingredient)


# 2. Магия для промежуточной таблицы (Ингредиент - Граммовка)
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 3  # Сколько пустых строчек для ингредиентов показывать по умолчанию


# 3. Настройка отображения самого Рецепта в админке
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Какие колонки показывать в общем списке рецептов
    list_display = ('name', 'category')

    # По какому полю делать поиск (удобно, если рецептов будет много)
    search_fields = ('name', 'description')

    # По какой колонке делать фильтрацию справа
    list_filter = ('category',)

    # ПОДКЛЮЧАЕМ МАГИЮ: ингредиенты будут редактироваться прямо внутри рецепта!
    inlines = [RecipeIngredientInline]
