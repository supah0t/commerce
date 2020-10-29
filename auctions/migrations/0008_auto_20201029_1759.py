# Generated by Django 3.1.2 on 2020-10-29 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201029_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='auction_listings',
            name='winner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]