# Generated by Django 4.0 on 2021-12-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]