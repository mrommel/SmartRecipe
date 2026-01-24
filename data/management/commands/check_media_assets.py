import os

from django.core.management import BaseCommand

from data.models import Recipe, Ingredient
from data.utils import blue_chunked_bar
from smartrecipe import settings


class Command(BaseCommand):
	def handle(self, **options):
		self.check_recipes_media_assets()
		self.check_ingredients_media_assets()

	def check_recipes_media_assets(self):
		recipeQs = Recipe.objects.all()
		totalRecipes = Recipe.objects.count()
		num_updated = 0

		for recipe in blue_chunked_bar(recipeQs, totalRecipes, 'Recipes'):
			# check for misplaced images
			if recipe.image.name.startswith('media/receipts/'):
				full_path = settings.MEDIA_ROOT + '/' + recipe.image.name
				new_path = settings.MEDIA_ROOT + '/' + recipe.image.name.replace('media/receipts/', 'media/recipes/')
				# print(f'Recipe ID: {recipe.id}, Name: {full_path}')
				os.system('mv %s %s' % (full_path, new_path))
				recipe.image.name = recipe.image.name.replace('media/receipts/', 'media/recipes/')
				recipe.save()
				num_updated += 1

			asset_name_jpg = f'/{recipe.id}.jpg'
			asset_name_jpeg = f'/{recipe.id}.jpeg'
			if not recipe.image.name.endswith(asset_name_jpg) and not recipe.image.name.endswith(asset_name_jpeg):
				print(f'WARNING: Recipe ID: {recipe.id} has unexpected image name: {recipe.image.name} => renaming')
				new_image_name = f'media/recipes{asset_name_jpg}'
				full_path = settings.MEDIA_ROOT + '/' + recipe.image.name
				new_path = settings.MEDIA_ROOT + '/' + new_image_name
				os.system('mv %s %s' % (full_path, new_path))
				recipe.image.name = new_image_name
				recipe.save()
				num_updated += 1

		print(f'Total Recipes: {totalRecipes:,}')
		print(f'Updated Recipes: {num_updated:,}')
		print()

	def check_ingredients_media_assets(self):
		ingredientQs = Ingredient.objects.all()
		totalIngredients = Ingredient.objects.count()
		num_updated = 0

		for ingredient in blue_chunked_bar(ingredientQs, totalIngredients, 'Ingredients'):
			if ingredient.image is None or ingredient.image.name == '':
				continue

			# check for misplaced images
			if ingredient.image.name.startswith('media/integrients/'):
				full_path = settings.MEDIA_ROOT + '/' + ingredient.image.name
				new_path = settings.MEDIA_ROOT + '/' + ingredient.image.name.replace('media/integrients/', 'media/ingredients/')
				# print(f'Ingredient ID: {ingredient.id}, Name: {full_path}')
				os.system('mv %s %s' % (full_path, new_path))
				ingredient.image.name = ingredient.image.name.replace('media/integrients/', 'media/ingredients/')
				ingredient.save()
				num_updated += 1

			asset_name_jpg = f'/{ingredient.id}.jpg'
			asset_name_png = f'/{ingredient.id}.png'

			if not ingredient.image.name.endswith(asset_name_jpg) and not ingredient.image.name.endswith(asset_name_png):
				print(f'WARNING: Ingredient ID: {ingredient.id} has unexpected image name: {ingredient.image.name} => renaming')
				if ingredient.image.name.endswith('.png'):
					new_image_name = f'media/ingredients{asset_name_png}'
				else:
					new_image_name = f'media/ingredients{asset_name_jpg}'

				full_path = settings.MEDIA_ROOT + '/' + ingredient.image.name
				new_path = settings.MEDIA_ROOT + '/' + new_image_name
				os.system('mv %s %s' % (full_path, new_path))
				ingredient.image.name = new_image_name
				ingredient.save()
				num_updated += 1

		print(f'Total Ingredients: {totalIngredients:,}')
		print(f'Updated Ingredients: {num_updated:,}')
		print()

