# Generated by Django 3.1.3 on 2020-11-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20200616_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptingredientrelation',
            old_name='integrient',
            new_name='ingredient',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/ingredients'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='important',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_type', to='data.ingredienttype'),
        ),
        migrations.AlterField(
            model_name='receiptcategory',
            name='is_country',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='receiptingredientrelation',
            name='amount_type',
            field=models.CharField(choices=[('K', 'Kilogramm'), ('G', 'Gramm'), ('L', 'Liter'), ('M', 'Milliliter'), ('T', 'TL'), ('E', 'EL'), ('S', 'Stück'), ('B', 'Becher'), ('P', 'Prise(n)'), ('C', 'Päckchen'), ('F', 'Flasche(n)'), ('N', 'Scheibe(n)'), ('W', 'Etwas'), ('D', 'Dose'), ('X', 'Glas'), ('R', 'Tasse')], max_length=1),
        ),
    ]
