# Generated by Django 4.0 on 2021-12-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_botuser_full_name_alter_botuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
