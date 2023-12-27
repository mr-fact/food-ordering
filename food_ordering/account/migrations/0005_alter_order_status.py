# Generated by Django 5.0 on 2023-12-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_order_paid_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'ثبت شده'), (2, 'تایید شده'), (3, 'ارسال شده'), (4, 'دریافت شده'), (5, 'کنسل شده')], default=1),
        ),
    ]