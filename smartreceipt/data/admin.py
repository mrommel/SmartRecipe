from django.contrib import admin

# Register your models here.
from data.models import IntegrientType, Integrient, Receipt, ReceiptIntegrientRelation, ReceiptCategory, ReceiptCategoryRelation
from data.forms import ReceiptAdmin

admin.site.register(IntegrientType)
admin.site.register(Integrient)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ReceiptIntegrientRelation)
admin.site.register(ReceiptCategory)
admin.site.register(ReceiptCategoryRelation)

