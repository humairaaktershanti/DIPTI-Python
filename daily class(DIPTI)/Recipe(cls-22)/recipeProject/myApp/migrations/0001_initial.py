# Generated by Django 5.2.3 on 2025-06-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecipeTitle', models.TextField(max_length=50)),
                ('RecipeImage', models.ImageField(upload_to='media/photo')),
                ('Ingredients', models.CharField(max_length=100)),
                ('Instruction', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
