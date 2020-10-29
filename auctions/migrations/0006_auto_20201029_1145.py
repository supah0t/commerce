# Generated by Django 3.1.2 on 2020-10-29 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201029_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='auction_listings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]