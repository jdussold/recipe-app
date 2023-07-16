from django.test import TestCase
from ingredients.models import Ingredient
from recipeingredients.models import RecipeIngredient
from recipes.models import Recipe
from django.shortcuts import reverse

# Create your tests here.


class RecipeModelTest(TestCase):
    def test_recipe_string_representation(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        self.assertEqual(str(recipe), "Test Recipe")

    # test for recipe difficulty (easy)
    def test_recipe_easy_difficulty(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=5, description="Test description"
        )
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)

        # force the recipe to update its difficulty level after ingredients are added
        recipe.save()

        self.assertEqual(recipe.difficulty, "Easy")

    # test for recipe difficulty (medium)
    def test_recipe_medium_difficulty(self):
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        ingredient3 = Ingredient.objects.create(name="Ingredient 3")
        ingredient4 = Ingredient.objects.create(name="Ingredient 4")
        ingredient5 = Ingredient.objects.create(name="Ingredient 5")

        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=5, description="Test description"
        )

        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient3)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient4)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient5)

        # force the recipe to update its difficulty level after ingredients are added
        recipe.save()

        self.assertEqual(recipe.difficulty, "Medium")

    # test for recipe difficulty (intermediate)
    def test_recipe_intermediate_difficulty(self):
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        ingredient3 = Ingredient.objects.create(name="Ingredient 3")

        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=15, description="Test description"
        )

        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient3)

        # force the recipe to update its difficulty level after ingredients are added
        recipe.save()

        self.assertEqual(recipe.difficulty, "Intermediate")

    # test for recipe difficulty (hard)
    def test_recipe_hard_difficulty(self):
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        ingredient3 = Ingredient.objects.create(name="Ingredient 3")
        ingredient4 = Ingredient.objects.create(name="Ingredient 4")
        ingredient5 = Ingredient.objects.create(name="Ingredient 5")

        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )

        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient3)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient4)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient5)

        # force the recipe to update its difficulty level after ingredients are added
        recipe.save()

        self.assertEqual(recipe.difficulty, "Hard")

    # test the recipe ingredients relationship
    def test_recipe_ingredients(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient1)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient2)
        self.assertEqual(recipe.ingredients.count(), 2)

    # test get_absolute_url
    def test_get_absolute_url(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        self.assertEqual(recipe.get_absolute_url(), "/recipes/1")

    # test RecipesListView
    def test_recipes_list_view(self):
        response = self.client.get("/recipes/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_list.html")

    # test context data in RecipesListView
    def test_recipes_list_view_context_data(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        response = self.client.get("/recipes/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["recipes"]), 1)
        self.assertEqual(response.context["recipes"][0], recipe)

    # test RecipesDetailView
    def test_recipes_detail_view(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        response = self.client.get("/recipes/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_detail.html")

    # test context data in RecipesDetailView
    def test_recipes_detail_view_context_data(self):
        recipe = Recipe.objects.create(
            id=1, title="Test Recipe", cooking_time=30, description="Test description"
        )
        response = self.client.get("/recipes/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["recipe"], recipe)

    # test recipes_home_view
    def test_recipes_home_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_home.html")
