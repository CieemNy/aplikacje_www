# Generated by Django 4.1.2 on 2022-11-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_osoba_miesiac_urodzenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_urodzenia',
            field=models.CharField(choices=[('1', 'styczeń'), ('2', 'luty'), ('3', 'marzec'), ('4', 'kwiecień'), ('5', 'maj'), ('6', 'czerwiec'), ('7', 'lipiec'), ('8', 'sierpień'), ('9', 'wrzesień'), ('10', 'październik'), ('11', 'listopad'), ('12', 'grudzień')], default=11, max_length=255),
        ),
    ]
