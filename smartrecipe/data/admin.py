from django.contrib import admin

# Register your models here.
from . import models
from .forms import ReceiptAdmin, IngredientAdmin, ReceiptCategoryAdmin

admin.site.register(models.IngredientType)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Receipt, ReceiptAdmin)
admin.site.register(models.ReceiptIngredientRelation)
admin.site.register(models.ReceiptCategory, ReceiptCategoryAdmin)
admin.site.register(models.ReceiptCategoryRelation)
admin.site.register(models.ReceiptTopic)

