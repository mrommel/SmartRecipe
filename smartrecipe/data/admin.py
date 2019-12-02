from django.contrib import admin

# Register your models here.
from data.models import IntegrientType, Integrient, Receipt, ReceiptIntegrientRelation, ReceiptCategory, ReceiptCategoryRelation, ReceiptTopic
from data.forms import ReceiptAdmin, IntegrientAdmin, ReceiptCategoryAdmin

admin.site.register(IntegrientType)
admin.site.register(Integrient, IntegrientAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ReceiptIntegrientRelation)
admin.site.register(ReceiptCategory, ReceiptCategoryAdmin)
admin.site.register(ReceiptCategoryRelation)
admin.site.register(ReceiptTopic)

