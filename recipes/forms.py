from django import forms
from .models import Ingredient

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
