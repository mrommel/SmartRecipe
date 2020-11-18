from django.contrib import admin

# Register your models here.

from .forms import RecipeAdmin, IngredientAdmin, IngredientTypeAdmin, RecipeCategoryAdmin, RecipeBookAdmin
from .models import IngredientType, Ingredient, Recipe, RecipeIngredientRelation, RecipeCategory, \
    RecipeCategoryRelation, RecipeTopic, RecipeBook

admin.site.register(RecipeBook, RecipeBookAdmin)
admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredientRelation)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
admin.site.register(RecipeCategoryRelation)
admin.site.register(RecipeTopic)

