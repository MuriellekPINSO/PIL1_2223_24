# Generated by Django 4.2.2 on 2023-06-23 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0018_remove_programme_publich"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="enseignant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.enseignant",
            ),
        ),
    ]