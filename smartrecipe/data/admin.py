from django.contrib import admin

# Register your models here.

from .forms import ReceiptAdmin, IngredientAdmin, IngredientTypeAdmin, ReceiptCategoryAdmin
from .models import IngredientType, Ingredient, Receipt, ReceiptIngredientRelation, ReceiptCategory, \
    ReceiptCategoryRelation, ReceiptTopic

admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ReceiptIngredientRelation)
admin.site.register(ReceiptCategory, ReceiptCategoryAdmin)
admin.site.register(ReceiptCategoryRelation)
admin.site.register(ReceiptTopic)

