# Generated by Django 4.1.2 on 2022-10-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_urodzenia',
            field=models.IntegerField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')]),
        ),
    ]