# Generated by Django 5.2.4 on 2025-07-19 06:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer_app', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('dath_of_birth', models.DateField(null=True)),
                ('candidate_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jobApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_education', models.CharField(max_length=100, null=True)),
                ('wark_experience', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('applied', 'applied'), ('interview', 'interview'), ('offered', 'offered'), ('rejected', 'rejected')], max_length=100, null=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate_app.candidateprofilemodel')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer_app.jobmodel')),
            ],
        ),
    ]
