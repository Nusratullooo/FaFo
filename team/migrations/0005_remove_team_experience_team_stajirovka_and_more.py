# Generated by Django 4.0 on 2021-12-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_remove_team_slug_alter_team_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='experience',
        ),
        migrations.AddField(
            model_name='team',
            name='stajirovka',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.IntegerField(blank=True, max_length=55),
        ),
    ]
