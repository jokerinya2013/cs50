# Generated by Django 3.1.4 on 2020-12-15 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201215_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='start_price',
            new_name='price',
        ),
    ]