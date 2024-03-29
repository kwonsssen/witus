# Generated by Django 2.2.6 on 2019-10-31 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket_team',
            old_name='team_name',
            new_name='basket_team_name',
        ),
        migrations.CreateModel(
            name='Mercenary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_kind', models.CharField(choices=[('basket', '농구'), ('foot', '족구'), ('soccer', '축구')], max_length=10, verbose_name='sport_kind')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='일정')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='용병_유저네임')),
            ],
        ),
    ]
