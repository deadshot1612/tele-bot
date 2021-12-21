# Generated by Django 4.0 on 2021-12-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('ru', 'Russian'), ('en', 'English'), ('uz', 'Uzbek')], default='ru', max_length=2)),
                ('full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
            ],
        ),
    ]