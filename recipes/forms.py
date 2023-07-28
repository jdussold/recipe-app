from django import forms
from .models import Ingredient, Recipe

CHART_CHOICES = (
    ("#1", "Bar Chart"),
    ("#2", "Pie Chart"),
    ("#3", "Line Chart"),
)


class RecipeSearchForm(forms.Form):
    Recipe_Name = forms.CharField(
        required=False,
        max_length=50,
        label="Recipe Name",
        widget=forms.TextInput(
            attrs={"class": "form-item", "placeholder": "Enter a Recipe Name"}
        ),
    )
    Ingredients = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Ingredient.objects.all(),
        label="Ingredient(s)",
        widget=forms.SelectMultiple(attrs={"class": "form-item"}),
    )
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES, widget=forms.Select(attrs={"class": "form-item"})
    )

    def clean(self):
        cleaned_data = super().clean()
        recipe_name = cleaned_data.get("Recipe_Name")
        ingredients = cleaned_data.get("Ingredients")

        if not recipe_name and not ingredients:
            raise forms.ValidationError(
                "Please enter a recipe name or select an ingredient."
            )
        return cleaned_data


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ["difficulty"]  # Exclude the 'difficulty' field from the form
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-item"}),
            "cooking_time": forms.NumberInput(attrs={"class": "form-item"}),
            "description": forms.Textarea(attrs={"class": "form-item"}),
            "ingredients": forms.SelectMultiple(
                attrs={
                    "class": "form-item",
                    "title": "Please select an item from the list. Hold CTRL to select multiple items",
                }
            ),
            "pic": forms.FileInput(attrs={"class": "form-item"}),
        }


class NewIngredientForm(forms.Form):
    new_ingredient = forms.CharField(
        max_length=255,
        required=False,
        help_text="Add a new ingredient",
        widget=forms.TextInput(attrs={"class": "form-item"}),
    )
