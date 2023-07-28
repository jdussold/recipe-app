from django.test import TestCase
from .models import Ingredient
from .forms import RecipeSearchForm, RecipeForm, NewIngredientForm


class NewIngredientFormTest(TestCase):
    def test_empty_form(self):
        form = NewIngredientForm(data={})
        self.assertTrue(
            form.is_valid()
        )  # Expect the form to be valid even if new_ingredient is empty.

    def test_valid_form(self):
        form_data = {"new_ingredient": "Tomato"}
        form = NewIngredientForm(data=form_data)
        self.assertTrue(form.is_valid())


class RecipeFormTest(TestCase):
    def test_invalid_form(self):
        form = RecipeForm(data={})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        form_data = {
            "title": "Pasta",
            "cooking_time": 10,
            "description": "A delicious pasta recipe",
            "ingredients": [ingredient.id],
        }
        form = RecipeForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())


class RecipeSearchFormTest(TestCase):
    def test_form_with_recipe_name(self):
        form_data = {"Recipe_Name": "Pasta", "chart_type": "#1"}
        form = RecipeSearchForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_with_ingredients(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        form_data = {"Ingredients": [ingredient.id], "chart_type": "#1"}
        form = RecipeSearchForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_with_no_data(self):
        form = RecipeSearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)  # Expected number of errors.

    def test_form_with_both_recipe_name_and_ingredients(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        form_data = {
            "Recipe_Name": "Pasta",
            "Ingredients": [ingredient.id],
            "chart_type": "#1",
        }
        form = RecipeSearchForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
