# ingredients/models.py

from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        "recipes.Recipe", on_delete=models.CASCADE, related_name="ingredients_used"
    )
    ingredient = models.ForeignKey(
        "ingredients.Ingredient",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes_used",
    )

    def __str__(self):
        return f"{self.ingredient} - {self.recipe}"
