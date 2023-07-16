from django.contrib import admin
from .models import Recipe, RecipeIngredient
from ingredients.models import Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)


admin.site.register(Recipe, RecipeAdmin)
