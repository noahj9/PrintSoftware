# Generated by Django 4.0.6 on 2022-08-28 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dockets', '0005_docket_deposit_amount_docket_quote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docket',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]