# Generated by Django 5.2.3 on 2025-06-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='Category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='Description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='Ingredients',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='Instruction',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='RecipeImage',
            field=models.ImageField(null=True, upload_to='media/photo'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='RecipeTitle',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
