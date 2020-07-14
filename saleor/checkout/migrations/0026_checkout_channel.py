# Generated by Django 3.0.6 on 2020-07-14 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0001_initial"),
        ("checkout", "0025_auto_20200221_0257"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="checkouts",
                to="channel.Channel",
            ),
        ),
    ]
