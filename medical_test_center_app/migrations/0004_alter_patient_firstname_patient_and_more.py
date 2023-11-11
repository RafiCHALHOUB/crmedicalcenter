# Generated by Django 4.1 on 2023-11-11 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_test_center_app', '0003_alter_patient_insured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='firstname_patient',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', message='Only letters and spaces are allowed.')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastname_patient',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', message='Only letters and spaces are allowed.')]),
        ),
    ]
