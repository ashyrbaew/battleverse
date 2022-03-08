# Generated by Django 3.0 on 2022-03-08 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('winner', models.CharField(blank=True, max_length=50)),
                ('is_active', models.CharField(blank=True, max_length=50)),
                ('player_first', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_user_first', to=settings.AUTH_USER_MODEL)),
                ('player_second', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_user_second', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'RPS Battle results',
            },
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_first_move', models.CharField(blank=True, max_length=50)),
                ('player_second_move', models.CharField(blank=True, max_length=50)),
                ('player_first_point', models.PositiveIntegerField(default=100)),
                ('player_second_point', models.PositiveIntegerField(default=100)),
                ('game_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_moves', to='mainapp.Battle')),
            ],
            options={
                'verbose_name': 'Moves',
            },
        ),
    ]
