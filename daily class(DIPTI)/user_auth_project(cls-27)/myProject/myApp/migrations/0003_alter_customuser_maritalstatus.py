# Generated by Django 5.2.3 on 2025-06-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_customuser_user_type_customuser_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='maritalStatus',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce')], max_length=100, null=True),
        ),
    ]
