from django.urls import path
from .views import (
    recipes_home,
    RecipesListView,
    RecipesDetailView,
    export_recipes_csv,
    generate_chart,
    about_page,
    add_recipe,
)

app_name = "recipes"

urlpatterns = [
    path("", recipes_home, name="recipes_home"),
    path("recipes/add/", add_recipe, name="add_recipe"),
    path("recipes/export/", export_recipes_csv, name="export_csv"),
    path("generate-chart/", generate_chart, name="generate_chart"),
    path("recipes/<int:pk>/", RecipesDetailView.as_view(), name="recipes_detail"),
    path("about/", about_page, name="about"),
    path("recipes/", RecipesListView.as_view(), name="recipes_list"),
]
