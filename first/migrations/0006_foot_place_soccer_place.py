# Generated by Django 2.2.6 on 2019-11-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20191031_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foot_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('x_coor', models.CharField(default=0, max_length=40, verbose_name='위도')),
                ('y_coor', models.CharField(default=0, max_length=40, verbose_name='경도')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
                ('discription', models.TextField(verbose_name='설명')),
                ('score', models.IntegerField(default=0, verbose_name='평점')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='first/%Y/%m/%d', verbose_name='프로필 사진')),
            ],
        ),
        migrations.CreateModel(
            name='Soccer_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('x_coor', models.CharField(default=0, max_length=40, verbose_name='위도')),
                ('y_coor', models.CharField(default=0, max_length=40, verbose_name='경도')),
                ('address', models.CharField(max_length=50, verbose_name='주소')),
                ('discription', models.TextField(verbose_name='설명')),
                ('score', models.IntegerField(default=0, verbose_name='평점')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='first/%Y/%m/%d', verbose_name='프로필 사진')),
            ],
        ),
    ]