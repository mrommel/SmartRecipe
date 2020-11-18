from django.contrib import admin

# Register your models here.

from .forms import RecipeAdmin, IngredientAdmin, IngredientTypeAdmin, ReceiptCategoryAdmin
from .models import IngredientType, Ingredient, Recipe, ReceiptIngredientRelation, RecipeCategory, \
    ReceiptCategoryRelation, ReceiptTopic

admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(ReceiptIngredientRelation)
admin.site.register(RecipeCategory, ReceiptCategoryAdmin)
admin.site.register(ReceiptCategoryRelation)
admin.site.register(ReceiptTopic)

