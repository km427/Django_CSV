# Generated by Django 2.2.7 on 2019-11-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=150),
        ),
    ]
