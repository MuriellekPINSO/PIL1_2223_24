# Generated by Django 4.2.2 on 2023-06-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0021_delete_programmefiliere"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programme",
            name="filiere",
        ),
    ]
