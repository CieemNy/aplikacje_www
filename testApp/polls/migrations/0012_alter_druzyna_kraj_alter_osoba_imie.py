# Generated by Django 4.1.2 on 2022-11-03 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_osoba_miesiac_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druzyna',
            name='kraj',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^[A-Z]+', 'Tylko duże litery')]),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='imie',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Tylko litery')]),
        ),
    ]
