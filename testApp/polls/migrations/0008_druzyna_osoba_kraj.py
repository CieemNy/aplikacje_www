# Generated by Django 4.1.2 on 2022-10-19 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_osoba_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('kraj', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^[A-Z]', 'Tylko duże litery')])),
            ],
        ),
        migrations.AddField(
            model_name='osoba',
            name='kraj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.druzyna'),
        ),
    ]