# Generated by Django 5.1.2 on 2024-10-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployementTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('agreed_salary', models.FloatField()),
                ('salary_start_date', models.DateField()),
                ('salary_end_date', models.DateField()),
            ],
        ),
    ]
