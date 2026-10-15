

from django.db import models

class IngredientCategory(models.Model):
    """Таблица для типов: Фрукт, Овощ, Орех и т.д."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    # Связь с таблицей категорий
    category = models.ForeignKey(
        IngredientCategory,
        on_delete=models.PROTECT,
        related_name='ingredients'
    )

    def __str__(self):
        return self.name

class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(RecipeCategory,on_delete=models.PROTECT)
    description = models.TextField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    def __str__(self):
        return self.name





class RecipeIngredient (models.Model):
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)


