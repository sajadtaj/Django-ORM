# Generated by Django 5.0.2 on 2024-02-24 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("OrmApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="album",
            table="Album",
        ),
        migrations.AlterModelTable(
            name="group",
            table="Group",
        ),
        migrations.AlterModelTable(
            name="membership",
            table="Membership",
        ),
        migrations.AlterModelTable(
            name="musician",
            table="Musician",
        ),
    ]
