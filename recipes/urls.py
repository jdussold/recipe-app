from django.urls import path
from .views import (
    recipes_home,
    RecipesListView,
    RecipesDetailView,
    export_recipes_csv,
    generate_chart,
)

app_name = "recipes"

urlpatterns = [
    path("", recipes_home, name="recipes_home"),
    path("recipes/", RecipesListView.as_view(), name="recipes_list"),
    path("recipes/export/", export_recipes_csv, name="export_csv"),
    path("generate-chart/", generate_chart, name="generate_chart"),
    path("recipes/<pk>/", RecipesDetailView.as_view(), name="recipes_detail"),
]
