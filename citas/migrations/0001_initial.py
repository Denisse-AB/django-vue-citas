# Generated by Django 4.0 on 2021-12-28 00:17

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Solo letras y espacios.')])),
                ('tel', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9 ]*$', 'Solo números permitidos.')])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
