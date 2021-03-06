# Generated by Django 4.0.5 on 2022-07-15 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sofy_pad_29',
            fields=[
                ('market_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('goods_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('goods_num', models.DecimalField(decimal_places=0, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_activity', models.CharField(default='none', max_length=10)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('goods_url', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['goods_price'],
            },
        ),
    ]
