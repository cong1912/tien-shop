# Generated by Django 3.0.6 on 2020-07-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="message",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
