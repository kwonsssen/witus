# Generated by Django 2.2.6 on 2019-11-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20191107_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercenary',
            name='sport_kind',
            field=models.CharField(choices=[('basket', '농구'), ('soccer', '축구'), ('foot', '족구')], max_length=10, verbose_name='sport_kind'),
        ),
    ]
