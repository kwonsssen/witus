# Generated by Django 2.2.6 on 2019-11-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20191111_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket_team_maching_sinchung',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]
