# Generated by Django 4.0 on 2021-12-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_remove_team_experience_team_stajirovka_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='stajirovka',
            new_name='experience',
        ),
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]