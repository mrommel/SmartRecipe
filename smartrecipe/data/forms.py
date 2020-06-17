from django.contrib import admin
from django import forms
import logging

from .models import ReceiptIngredientRelation, ReceiptCategoryRelation, Receipt, Ingredient, \
    ReceiptCategory, IngredientType

logger = logging.getLogger(__name__)


class IngredientTypeIngredientRelationInline(admin.TabularInline):
    model = Ingredient
    fk_name = "type"
    extra = 1


class IngredientTypeAdmin(admin.ModelAdmin):

    inlines = [
        IngredientTypeIngredientRelationInline,
    ]

    class Meta:
        model = IngredientType
        fields = ('name', )
        list_display = ('name', )


class ReceiptIngredientRelationInline(admin.TabularInline):
    model = ReceiptIngredientRelation
    fk_name = "receipt"
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 5


class ReceiptCategoryRelationInline(admin.TabularInline):
    model = ReceiptCategoryRelation
    fk_name = "receipt"
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 5


class ReceiptCategoryRelationInline2(admin.TabularInline):
    model = ReceiptCategoryRelation
    fk_name = "receiptCategory"
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 0


class ReceiptAdminForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('name', 'teaser', 'description', 'image', 'time', 'calories', 'portions',
                  'step0', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9')
        widgets = {
            'teaser': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step0': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step1': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step2': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step3': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step4': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step5': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step6': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step7': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step8': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'step9': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class ReceiptAdmin(admin.ModelAdmin):
    form = ReceiptAdminForm
    list_display = ('name', 'thumbnail', 'admin_steps_info', 'admin_ingredients_info', 'admin_categories')
    ordering = ('name',)
    inlines = [
        ReceiptIngredientRelationInline,
        ReceiptCategoryRelationInline,
    ]
    actions_on_top = True
    actions_on_bottom = True

    def admin_categories(self, instance):
        str_value = '<ul class="commalist">'
        for category in instance.categories():
            str_value = '%s<li><a href="/admin/data/receiptcategory/%d/change/">%s</a></li>' % (
                str_value, category.receiptCategory.id, category.receiptCategory.name)
        str_value = '%s</ul>' % str_value
        return str_value

    admin_categories.allow_tags = True
    admin_categories.short_description = 'categories'

    def admin_steps_info(self, instance):
        steps = len(instance.steps())
        if steps == 0:
            return '<span style="color:#f00;">no steps</span>'
        else:
            return '%d steps' % steps

    admin_steps_info.allow_tags = True
    admin_steps_info.short_description = '# steps'

    def admin_ingredients_info(self, instance):
        ingredients = len(instance.ingredients())
        if ingredients == 0:
            return '<span style="color:#f00;">no ingredients</span>'
        else:
            return '%d ingredients' % ingredients

    admin_ingredients_info.allow_tags = True
    admin_ingredients_info.short_description = '# ingredients'

    class Media:
        css = {
            'all': ('data/css/admin.css',)
        }


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', 'plural', 'thumbnail', 'type', 'important')
    ordering = ('name',)


class ReceiptCategoryAdmin(admin.ModelAdmin):
    model = ReceiptCategory
    list_display = ('thumbnail', 'name', 'path',)
    readonly_fields = ('thumbnail', 'path',)
    ordering = ('name',)

    inlines = [
        ReceiptCategoryRelationInline2,
    ]
