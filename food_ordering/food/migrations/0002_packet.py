# Generated by Django 5.0 on 2023-12-22 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_order'),
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packets', to='account.order')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packets', to='food.price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]