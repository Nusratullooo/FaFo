# Generated by Django 4.0 on 2021-12-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_team_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='biography',
            field=models.TextField(blank=True),
        ),
    ]
