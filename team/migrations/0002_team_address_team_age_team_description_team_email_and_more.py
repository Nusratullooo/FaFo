# Generated by Django 4.0 on 2021-12-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='address',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='team',
            name='age',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='team',
            name='experience',
            field=models.IntegerField(blank=True, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
