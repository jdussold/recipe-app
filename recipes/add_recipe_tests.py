from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, RecipeIngredient
from django.contrib.messages import get_messages


class AddRecipeViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        # Login the user
        self.client.login(username="testuser", password="testpassword")
        # Create a few ingredients for testing
        self.ingredient1 = Ingredient.objects.create(name="Egg")
        self.ingredient2 = Ingredient.objects.create(name="Salt")

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("recipes:add_recipe"))
        self.assertRedirects(response, "/login/?next=/recipes/add/")

    def test_get_form(self):
        response = self.client.get(reverse("recipes:add_recipe"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/add_recipe.html")

    def test_easy_difficulty(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Omelette",
                "cooking_time": 5,
                "description": "A simple omelette.",
                "ingredients": [self.ingredient1.id],
                "pic": "",
                "form-TOTAL_FORMS": "1",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Pepper",
            },
        )
        recipe = Recipe.objects.latest("id")
        self.assertEqual(recipe.difficulty, "Easy")

    def test_medium_difficulty(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Boiled Eggs",
                "cooking_time": 5,
                "description": "Tasty boiled eggs.",
                "ingredients": [self.ingredient1.id, self.ingredient2.id],
                "pic": "",
                "form-TOTAL_FORMS": "2",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Pepper",
                "form-1-new_ingredient": "Milk",
            },
        )
        recipe = Recipe.objects.latest("id")
        self.assertEqual(recipe.difficulty, "Medium")

    def test_intermediate_difficulty(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Egg Fry",
                "cooking_time": 15,
                "description": "Delicious egg fry.",
                "ingredients": [self.ingredient1.id],
                "pic": "",
                "form-TOTAL_FORMS": "1",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Oil",
            },
        )
        recipe = Recipe.objects.latest("id")
        self.assertEqual(recipe.difficulty, "Intermediate")

    def test_hard_difficulty(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Egg Delight",
                "cooking_time": 15,
                "description": "Complex egg delight.",
                "ingredients": [self.ingredient1.id, self.ingredient2.id],
                "pic": "",
                "form-TOTAL_FORMS": "2",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Pepper",
                "form-1-new_ingredient": "Milk",
            },
        )
        recipe = Recipe.objects.latest("id")
        self.assertEqual(recipe.difficulty, "Hard")

    def test_successful_recipe_addition(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Test Recipe",
                "cooking_time": 5,
                "description": "A test recipe",
                "ingredients": [self.ingredient1.id],
                "pic": "",
                "form-TOTAL_FORMS": "1",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Pepper",
            },
        )
        recipe = Recipe.objects.latest("id")
        self.assertRedirects(response, recipe.get_absolute_url())

    def test_save_and_add_another_functionality(self):
        response = self.client.post(
            reverse("recipes:add_recipe"),
            {
                "title": "Test Recipe 2",
                "cooking_time": 15,
                "description": "Another test recipe",
                "ingredients": [self.ingredient1.id, self.ingredient2.id],
                "pic": "",
                "save_and_add": True,
                "form-TOTAL_FORMS": "2",
                "form-INITIAL_FORMS": "0",
                "form-MIN_NUM_FORMS": "",
                "form-MAX_NUM_FORMS": "5",
                "form-0-new_ingredient": "Pepper",
                "form-1-new_ingredient": "Milk",
            },
        )
        self.assertRedirects(response, reverse("recipes:add_recipe"))

    def test_form_errors(self):
        response = self.client.post(reverse("recipes:add_recipe"), {})
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            "Form validation failed. Please check the entered data.",
            [str(m) for m in messages],
        )
