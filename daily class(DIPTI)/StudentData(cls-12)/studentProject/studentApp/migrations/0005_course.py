# Generated by Django 5.2.1 on 2025-06-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0004_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('Code', models.CharField(max_length=100, null=True)),
                ('credits', models.IntegerField(null=True)),
            ],
        ),
    ]
