# Generated by Django 4.2.2 on 2023-06-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0022_remove_programme_filiere"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="filieres",
            field=models.ManyToManyField(to="home.filiere"),
        ),
    ]
