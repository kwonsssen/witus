# Generated by Django 2.2.6 on 2019-11-08 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20191108_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_maching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_kind', models.CharField(choices=[('foot', '족구'), ('soccer', '축구'), ('basket', '농구')], max_length=10, verbose_name='sport_kind')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='post.Basket_Team', verbose_name='용병_유저네임')),
            ],
        ),
        migrations.DeleteModel(
            name='Mercenary',
        ),
    ]
