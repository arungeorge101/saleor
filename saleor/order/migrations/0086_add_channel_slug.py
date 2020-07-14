# Generated by Django 3.0.6 on 2020-07-14 08:25

from django.db import migrations


def add_channel_slug(apps, schema_editor):
    Channel = apps.get_model("channel", "Channel")
    Order = apps.get_model("order", "Order")

    if Order.objects.exists():
        channels_dict = {}

        for order in Order.objects.iterator():
            currency = order.currency
            channel = channels_dict.get(currency)

            if not channel:
                channel, _ = Channel.objects.get_or_create(
                    currency_code=currency,
                    defaults={
                        "name": f"Channel {currency}",
                        "slug": f"channel-{currency.lower()}",
                    },
                )
                channels_dict[currency] = channel

            order.channel = channel

            order.save(update_fields=["channel"])


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0001_initial"),
        ("order", "0085_order_channel"),
    ]

    operations = [migrations.RunPython(add_channel_slug)]
