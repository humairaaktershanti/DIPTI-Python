# Generated by Django 5.2.4 on 2025-07-08 03:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbookingmodel',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
