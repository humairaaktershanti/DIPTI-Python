# Generated by Django 5.2.4 on 2025-07-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jobApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_education', models.CharField(blank=True, max_length=255, null=True)),
                ('work_experience', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('interview', 'Interview'), ('offered', 'Offered'), ('rejected', 'Rejected')], default='applied', max_length=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
