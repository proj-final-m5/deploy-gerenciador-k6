# Generated by Django 4.1.5 on 2023-01-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invite",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
