# Generated by Django 5.2.1 on 2025-05-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0003_delete_addcourse_delete_addteacher_alter_student_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
