# Generated by Django 4.2.2 on 2023-07-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0024_communique"),
    ]

    operations = [
        migrations.AddField(
            model_name="cours",
            name="masse_horaire",
            field=models.IntegerField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="heure_fin",
            field=models.DateField(auto_now=True),
        ),
    ]
