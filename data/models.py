#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import logging
from html import escape

from django.db import models
from django.utils.safestring import mark_safe, SafeString

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RecipeBook(models.Model):
    """
        class of a recipe book
    """
    name = models.CharField(max_length=100)

    def recipes(self):

        recipe_list = []

        for recipeRelation in RecipeBookRecipeRelation.objects.filter(recipeBook=self):
            recipe_list.append(recipeRelation.recipe)

        return recipe_list

    def __str__(self):
        return '%s' % self.name


class IngredientType(models.Model):
    """
        class of a ingredient type
    """
    name = models.CharField(max_length=50)

    def url(self):
        if self.name is not None:
            return '/data/ingredient_type/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
        else:
            return '-'

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return '%s' % self.name


class Ingredient(models.Model):
    """
        class of a ingredient
    """
    name = models.CharField(max_length=50)
    plural = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, blank=True, null=True,
                             related_name="ingredient_type")
    image = models.ImageField(upload_to='media/ingredients', blank=True, null=True)
    important = models.BooleanField(default=False, blank=True, null=True)

    def thumbnail(self):
        if self.image.name is not None:
            return mark_safe('<img border="0" alt="" src="/media/%s" height="20" style="height: 20px;" />' % (
                escape(self.image.name)))
        else:
            return mark_safe('<img border="0" alt="" src="/media/none.png" height="20" style="height: 20px;" />')

    thumbnail.allow_tags = True
    thumbnail.short_description = 'thumbnail'

    def image_url(self):
        return '/media/%s' % self.image.name

    def receipts(self):
        return RecipeIngredientRelation.objects.filter(ingredient=self)

    def number_of_recipes(self):
        return len(self.recipes())

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return '%s' % self.name


class RecipeStep:
    index = 0
    text = ""

    def __init__(self, index_value, step_text):
        self.index = index_value
        self.text = step_text


class Recipe(models.Model):
    """
        class of a receipt
    """
    name = models.CharField(max_length=50)
    teaser = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=20000, blank=True, null=True)
    image = models.ImageField(upload_to='media/receipts', blank=True, null=True)
    time = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    portions = models.IntegerField(default=0)

    step0 = models.CharField(max_length=1000, blank=True, null=True)
    step1 = models.CharField(max_length=1000, blank=True, null=True)
    step2 = models.CharField(max_length=1000, blank=True, null=True)
    step3 = models.CharField(max_length=1000, blank=True, null=True)
    step4 = models.CharField(max_length=1000, blank=True, null=True)
    step5 = models.CharField(max_length=1000, blank=True, null=True)
    step6 = models.CharField(max_length=1000, blank=True, null=True)
    step7 = models.CharField(max_length=1000, blank=True, null=True)
    step8 = models.CharField(max_length=1000, blank=True, null=True)
    step9 = models.CharField(max_length=1000, blank=True, null=True)

    source = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def url(self):
        if self.name is not None:
            return '/data/recipe/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
        else:
            return '-'

    def image_url(self):
        return '/media/%s' % self.image.name

    def time_str(self):
        return u'%d min' % self.time

    def categories(self):
        return RecipeCategoryRelation.objects.filter(recipe=self)

    def ingredients(self):
        return RecipeIngredientRelation.objects.filter(recipe=self)

    def steps(self):
        steps = []

        if self.step0 is not None and self.step0 != '':
            steps.append(RecipeStep(1, self.step0))

        if self.step1 is not None and self.step1 != '':
            steps.append(RecipeStep(2, self.step1))

        if self.step2 is not None and self.step2 != '':
            steps.append(RecipeStep(3, self.step2))

        if self.step3 is not None and self.step3 != '':
            steps.append(RecipeStep(4, self.step3))

        if self.step4 is not None and self.step4 != '':
            steps.append(RecipeStep(5, self.step4))

        if self.step5 is not None and self.step5 != '':
            steps.append(RecipeStep(6, self.step5))

        if self.step6 is not None and self.step6 != '':
            steps.append(RecipeStep(7, self.step6))

        if self.step7 is not None and self.step7 != '':
            steps.append(RecipeStep(8, self.step7))

        if self.step8 is not None and self.step8 != '':
            steps.append(RecipeStep(9, self.step8))

        if self.step9 is not None and self.step9 != '':
            steps.append(RecipeStep(10, self.step9))

        return steps

    def countries(self):
        country_list = []

        for category in self.categories():
            if category.recipeCategory.is_country:
                country_list.append(category.recipeCategory)

        return country_list

    def thumbnail(self):
        if self.image.name is not None:
            return mark_safe('<img border="0" alt="" src="/media/%s" height="20" style="height: 20px;" />' % (
                escape(self.image.name)))
        else:
            return mark_safe('<img border="0" alt="" src="/media/none.png" height="20" style="height: 20px;" />')

    thumbnail.allow_tags = True
    thumbnail.short_description = 'thumbnail'

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ['name']


class RecipeBookRecipeRelation(models.Model):
    """
        class of a RecipeBookRecipeRelation
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipeBook = models.ForeignKey(RecipeBook, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s - %s' % (self.recipeBook.name, self.recipe.name)

    def __str__(self):
        return '%s - %s' % (self.recipeBook.name, self.recipe.name)


class RecipeIngredientRelation(models.Model):
    """
        class of a RecipeIngredientRelation
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    amount_type = models.CharField(max_length=1, choices=(
        ('K', 'Kilogramm'), ('G', 'Gramm'), ('L', 'Liter'), ('M', 'Milliliter'), ('T', 'TL'), ('E', 'EL'),
        ('S', 'Stück'),
        ('B', 'Becher'), ('P', 'Prise(n)'), ('C', 'Päckchen'), ('F', 'Flasche(n)'), ('N', 'Scheibe(n)'), ('W', 'Etwas'),
        ('D', 'Dose'), ('X', 'Glas'), ('R', 'Tasse')))

    def quantity(self):
        if self.amount_type == 'K':
            return '%1.1f Kg' % self.amount

        if self.amount_type == 'G':
            return '%d g' % self.amount

        if self.amount_type == 'L':
            return '%1.1f l' % self.amount

        if self.amount_type == 'M':
            return '%d ml' % self.amount

        if self.amount_type == 'T':
            return '%1.1f TL' % self.amount

        if self.amount_type == 'E':
            return '%d EL' % self.amount

        if self.amount_type == 'S':
            return '%d' % self.amount

        if self.amount_type == 'B':
            return '%d Becher' % self.amount

        if self.amount_type == 'P':
            if self.amount == 1:
                return '1 Prise'
            else:
                return '%d Prisen' % self.amount

        if self.amount_type == 'C':
            if self.amount == 0.5:
                return '1/2 Paeckchen'
            else:
                return '%d Paeckchen' % self.amount

        if self.amount_type == 'F':
            if self.amount == 0.5:
                return '1/2 Flasche'
            elif self.amount == 1:
                return '1 Flasche'
            elif int(self.amount) == self.amount:
                return '%d Flaschen' % self.amount
            else:
                return '%1.1f Flaschen' % self.amount

        if self.amount_type == 'N':
            return '%d Scheibe(n)' % self.amount

        if self.amount_type == 'W':
            return ''

        if self.amount_type == 'D':
            return '%d Dose(n)' % self.amount

        if self.amount_type == 'X':
            return '%d Glas' % self.amount

        if self.amount_type == 'R':
            if self.amount == 1.0:
                return '%d Tasse' % self.amount
            else:
                return '%d Tassen' % self.amount

        return '%1.1f %s' % (self.amount, self.get_amount_type_display())

    def is_plural(self):
        if self.amount_type == 'S':
            if self.amount > 1.0:
                return True

        return False

    def __unicode__(self):
        return u'%s - %s' % (self.recipe.name, self.ingredient.name)

    def __str__(self):
        return '%s - %s' % (self.recipe.name, self.ingredient.name)


class RecipeCategory(models.Model):
    """
        class of a RecipeCategory
    """
    name = models.CharField(max_length=50)
    parentRecipeCategory = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/category', blank=True, null=True)
    is_country = models.BooleanField(default=False, blank=True, null=True)

    def thumbnail(self):
        return SafeString('<img border="0" alt="" src="/media/%s" height="20" style="height:20px" />' % self.image.name)

    thumbnail.allow_tags = True

    def parent_id(self):
        if self.parentRecipeCategory is None:
            return -1
        else:
            return self.parentRecipeCategory.id

    def path(self):
        if self.parentRecipeCategory is None:
            return self.name
        else:
            return u'%s - %s' % (self.parentRecipeCategory.path(), self.name)

    def url(self):
        if self.name is not None:
            return '/data/category/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
        else:
            return '-'

    def image_url(self):
        return '/media/%s' % self.image.name

    def children(self):
        return RecipeCategory.objects.filter(parentRecipeCategory=self)

    def recipes(self):
        return RecipeCategoryRelation.objects.filter(recipeCategory=self)

    def main_recipes(self):
        main_recipes_list = []

        for relation in RecipeCategoryRelation.objects.filter(recipeCategory=self):
            if relation.is_main:
                main_recipes_list.append(relation)

        return  main_recipes_list

    def number_of_recipes(self):
        num = len(self.recipes())

        for child in RecipeCategory.objects.filter(parentRecipeCategory=self):
            num = num + child.number_of_recipes()

        return num

    def number_of_main_recipes(self):
        num = len(self.main_recipes())

        for child in RecipeCategory.objects.filter(parentRecipeCategory=self):
            num = num + child.number_of_main_recipes()

        return num

    #def admin_url(self):
    #    return mark_safe('<a href="%s">%s</a>' % (self.id, self.name))

    #admin_url.allow_tags = True

    def __unicode__(self):
        return u'%s' % (self.path())

    def __str__(self):
        return '%s' % (self.path())

    class Meta:
        ordering = ['name']


class RecipeCategoryRelation(models.Model):
    """
        class of a RecipeIngredientRelation
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipeCategory = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, blank=True, null=True)

    def __unicode__(self):
        return u'%s -> %s' % (self.recipe, self.recipeCategory)

    def __str__(self):
        return '%s -> %s' % (self.recipe, self.recipeCategory)

    class Meta:
        ordering = ['recipe__name']


class RecipeTopic(models.Model):
    """
        class of a RecipeTopic
    """
    name = models.CharField(max_length=50)
    parentRecipeTopic = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def path(self):
        if self.parentRecipeTopic is None:
            return self.name
        else:
            return u'%s - %s' % (self.parentRecipeTopic.path(), self.name)

    def url(self):
        if self.name is not None:
            return '/data/topic/%d/%s.html' % (self.id, self.name.replace(' ', '_').lower())
        else:
            return '-'

    def children(self):
        return RecipeTopic.objects.filter(parentRecipeTopic=self)

    def recipes(self):
        return RecipeTopicRelation.objects.filter(recipeTopic=self)

    def __unicode__(self):
        return u'%s' % (self.path())

    def __str__(self):
        return '%s' % (self.path())


class RecipeTopicRelation(models.Model):
    """
        class of a RecipeTopicRelation
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipeTopic = models.ForeignKey(RecipeTopic, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s -> %s' % (self.recipe, self.recipeTopic)

    def __str__(self):
        return '%s -> %s' % (self.recipe, self.recipeTopic)
