# Generated by Django 3.1.2 on 2020-10-29 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201029_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='winner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
