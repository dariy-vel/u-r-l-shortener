# Generated by Django 2.0.1 on 2018-06-29 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LongToShortURL', '0004_auto_20180629_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longtoshort',
            name='owner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
