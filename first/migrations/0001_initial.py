# Generated by Django 2.2.6 on 2019-10-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('x_coor', models.IntegerField(default=0, verbose_name='위도')),
                ('y_coor', models.IntegerField(default=0, verbose_name='경도')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
                ('description', models.TextField(verbose_name='설명')),
                ('score', models.IntegerField(default=0, verbose_name='평점')),
            ],
        ),
    ]
