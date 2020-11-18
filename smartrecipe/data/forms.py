from django.contrib import admin
from django import forms
import logging

from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeString

from .models import RecipeIngredientRelation, RecipeCategoryRelation, Recipe, Ingredient, \
    RecipeCategory, IngredientType, RecipeBook, RecipeBookRecipeRelation

logger = logging.getLogger(__name__)


class RecipeBookRecipeRelationInline(admin.TabularInline):
    model = RecipeBookRecipeRelation
    fk_name = "recipeBook"
    extra = 1


class RecipeBookAdmin(admin.ModelAdmin):

    list_display = ('name', 'number_of_recipes', 'book_actions')
    inlines = [
        RecipeBookRecipeRelationInline,
    ]

    def number_of_recipes(self, instance):
        recipes = len(instance.recipes())
        if recipes == 0:
            return SafeString('<span style="color:#f00;">no recipes</span>')
        else:
            return '%d recipes' % recipes

    number_of_recipes.allow_tags = True
    number_of_recipes.short_description = '# recipes'

    def book_actions(self, instance):
        return SafeString('<a href="/data/export/%d/recipes/" target="_blank">Export as PDF</a>' % instance.id)

    book_actions.allow_tags = True
    book_actions.short_description = 'Book Actions'

    class Meta:
        model = RecipeBook
        fields = ('name', )
        list_display = ('name', )


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
    model = RecipeIngredientRelation
    fk_name = "recipe"
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 5


class RecipeCategoryRelationInline(admin.TabularInline):
    model = RecipeCategoryRelation
    fk_name = "recipe"
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 5


class RecipeCategoryRelationInline2(admin.TabularInline):
    model = RecipeCategoryRelation
    fk_name = "recipeCategory"
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        """ hide all extra if the current user is having the wrong gender """
        return 0


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
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


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    list_display = ('name', 'thumbnail', 'admin_steps_info', 'admin_ingredients_info', 'admin_categories')
    ordering = ('name',)
    inlines = [
        ReceiptIngredientRelationInline,
        RecipeCategoryRelationInline,
    ]
    actions_on_top = True
    actions_on_bottom = True

    def admin_categories(self, instance):
        str_value = '<ul class="commalist">'
        for category in instance.categories():
            str_value = '%s<li><a href="/admin/data/recipecategory/%d/change/">%s</a></li>' % (
                str_value, category.recipeCategory.id, category.recipeCategory.name)
        str_value = '%s</ul>' % str_value
        return SafeString(str_value)

    admin_categories.allow_tags = True
    admin_categories.short_description = 'categories'

    def admin_steps_info(self, instance):
        steps = len(instance.steps())
        if steps == 0:
            return SafeString('<span style="color:#f00;">no steps</span>')
        else:
            return '%d steps' % steps

    admin_steps_info.allow_tags = True
    admin_steps_info.short_description = '# steps'

    def admin_ingredients_info(self, instance):
        ingredients = len(instance.ingredients())
        if ingredients == 0:
            return SafeString('<span style="color:#f00;">no ingredients</span>')
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


class RecipeCategoryAdmin(admin.ModelAdmin):
    model = RecipeCategory
    list_display = ('thumbnail', 'name', 'path',)
    readonly_fields = ('thumbnail', 'path',)
    ordering = ('name',)

    inlines = [
        RecipeCategoryRelationInline2,
    ]
