# Generated by Django 5.2.3 on 2025-06-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_rename_relationshipstatus_customuser_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profileimage',
            field=models.ImageField(null=True, upload_to='Media/photo'),
        ),
    ]
