# Generated by Django 3.2.13 on 2022-05-17 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0010_rename_email_informations_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informations',
            old_name='departement',
            new_name='department',
        ),
    ]