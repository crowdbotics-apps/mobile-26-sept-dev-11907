# Generated by Django 2.2.16 on 2020-09-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customtext",
            name="title",
        ),
        migrations.AddField(
            model_name="customtext",
            name="gffhgfhgfhfgfhf",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
