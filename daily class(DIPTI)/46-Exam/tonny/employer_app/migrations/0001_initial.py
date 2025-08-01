# Generated by Django 5.2.4 on 2025-07-19 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('about_company', models.CharField(max_length=250, null=True)),
                ('company_logo', models.ImageField(null=True, upload_to='media/image')),
                ('location', models.CharField(max_length=250, null=True)),
                ('employer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('job_type', models.CharField(choices=[('Full_Time', 'Full_Time'), ('Remote', 'Remote'), ('Internship', 'Internship')], max_length=100, null=True)),
                ('title', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('requirements', models.CharField(max_length=250, null=True)),
                ('salary', models.CharField(max_length=150, null=True)),
                ('deadline', models.DateField(auto_now=True, null=True)),
                ('posted_date', models.DateField(auto_now=True, null=True)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer_app.employerprofilemodel')),
            ],
        ),
    ]
