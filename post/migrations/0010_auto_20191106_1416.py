# Generated by Django 2.2.6 on 2019-11-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20191106_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercenary',
            name='sport_kind',
            field=models.CharField(choices=[('foot', '족구'), ('basket', '농구'), ('soccer', '축구')], max_length=10, verbose_name='sport_kind'),
        ),
    ]
