from io import BytesIO
import base64
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from django.http import HttpResponse, JsonResponse, Http404
import matplotlib.pyplot as plt
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")


def render_chart(chart_type, data, **kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(12, 8), dpi=100)
    ax = fig.add_subplot(111)

    if chart_type == "#1":
        # Bar Chart
        plt.title("Cooking Time by Recipe", fontsize=20)
        plt.bar(data["title"], data["cooking_time"])
        plt.xlabel("Recipes", fontsize=16)
        plt.ylabel("Cooking Time (min)", fontsize=16)
    elif chart_type == "#2":
        # Pie Chart
        plt.title("Recipes Cooking Time Comparison", fontsize=20)
        labels = kwargs.get("labels")
        plt.pie(data["cooking_time"], labels=None, autopct="%1.1f%%")
        plt.legend(
            data["title"],
            loc="upper right",
            bbox_to_anchor=(1.0, 1.0),
            fontsize=12,
        )
    elif chart_type == "#3":
        # Line Chart
        plt.title("Cooking Time by Recipe", fontsize=20)
        x_values = data["title"].to_numpy()  # Convert to numpy array
        y_values = data["cooking_time"].to_numpy()  # Convert to numpy array
        plt.plot(x_values, y_values)
        plt.xlabel("Recipes", fontsize=16)
        plt.ylabel("Cooking Time (min)", fontsize=16)
    else:
        print("Unknown chart type.")

    plt.tight_layout(pad=3.0)

    # Convert the plot to an image
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.read()).decode("utf-8")

    return chart_image


class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"
    context_object_name = "recipes"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_name = self.request.GET.get("Recipe_Name")
        ingredients = self.request.GET.getlist("Ingredients")

        if recipe_name:
            queryset = queryset.filter(title__icontains=recipe_name)

        if ingredients:
            for ingredient in ingredients:
                queryset = queryset.filter(ingredients__id=ingredient)

        # Check if there are any recipes in the queryset
        if not queryset.exists():
            # Add a message to the user indicating no recipes found
            messages.warning(
                self.request,
                "There are no recipes with that combination of ingredients.",
            )
            # Return an empty queryset
            queryset = Recipe.objects.none()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Convert the QuerySet to a pandas DataFrame
            df = pd.DataFrame.from_records(context["recipes"].values())
            context["recipes_df"] = df

            context["form"] = RecipeSearchForm(self.request.GET)

            # Generate and pass the chart paths to the context
            chart_type = self.request.GET.get("chart_type")
            if chart_type:
                chart_data = {"title": df["title"], "cooking_time": df["cooking_time"]}
                if chart_type == "#1":
                    chart_data["labels"] = df["title"]
                elif chart_type == "#2":
                    chart_data["labels"] = df["title"]
                else:
                    chart_data["labels"] = None

                chart_image = render_chart(chart_type, chart_data)
                context["chart_image"] = chart_image

        except KeyError:
            # If KeyError occurs, handle the error and set the appropriate context variables
            context["recipes"] = []  # Set an empty list to recipes
            context[
                "error_message"
            ] = "There are no recipes with that combination of ingredients."

        # Pagination
        paginator = Paginator(context["recipes"], self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj

        return context


def export_recipes_csv(request):
    # Get the filter parameters from the request
    recipe_name = request.GET.get("Recipe_Name")
    ingredients = request.GET.getlist("Ingredients")

    # Filter the Recipe objects based on the request parameters
    queryset = Recipe.objects.all()

    if recipe_name:
        queryset = queryset.filter(title__icontains=recipe_name)

    if ingredients:
        for ingredient in ingredients:
            # Check if the ingredient parameter is empty
            if ingredient:
                queryset = queryset.filter(ingredients__id=ingredient)

    # Convert the filtered QuerySet to a list of dictionaries
    recipe_data = list(queryset.values())

    # Get the related Ingredient data for each recipe
    for data in recipe_data:
        recipe = Recipe.objects.get(pk=data["id"])
        data["ingredients"] = ", ".join(
            [ingredient.name for ingredient in recipe.ingredients.all()]
        )

    # Create the DataFrame from the list of dictionaries
    df = pd.DataFrame.from_records(recipe_data)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="recipes.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


def generate_chart(request):
    chart_type = request.GET.get("chart_type")
    recipe_name = request.GET.get("Recipe_Name")
    ingredients = request.GET.getlist("Ingredients")

    # Filter the Recipe objects based on the request parameters
    queryset = Recipe.objects.all()

    if recipe_name:
        queryset = queryset.filter(title__icontains=recipe_name)

    if ingredients:
        for ingredient in ingredients:
            # Check if the ingredient parameter is empty
            if ingredient:
                queryset = queryset.filter(ingredients__id=ingredient)

    # Convert the filtered QuerySet to a list of dictionaries
    recipe_data = list(queryset.values())

    # Get the related Ingredient data for each recipe
    for data in recipe_data:
        recipe = Recipe.objects.get(pk=data["id"])
        data["ingredients"] = ", ".join(
            [ingredient.name for ingredient in recipe.ingredients.all()]
        )

    # Create the DataFrame from the list of dictionaries
    df = pd.DataFrame.from_records(recipe_data)

    chart_data = {"title": df["title"], "cooking_time": df["cooking_time"]}
    if chart_type == "#1":
        chart_data["labels"] = df["title"]
    elif chart_type == "#2":
        # For Pie Chart, labels should be the recipe titles, and not the cooking times
        chart_data["labels"] = df["title"]
    else:
        chart_data["labels"] = None

    chart_image = render_chart(chart_type, chart_data)
    return JsonResponse({"chart_image": chart_image})


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
    context_object_name = "recipe"
