# Generated by Django 3.2.13 on 2022-05-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0005_auto_20220517_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='informations',
            name='IDS',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='informations',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
