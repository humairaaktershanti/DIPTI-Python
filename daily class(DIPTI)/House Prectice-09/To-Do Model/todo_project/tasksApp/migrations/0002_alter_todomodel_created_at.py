# Generated by Django 5.2.1 on 2025-06-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
