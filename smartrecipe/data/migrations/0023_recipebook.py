# Generated by Django 3.1.3 on 2020-11-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_auto_20201118_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
