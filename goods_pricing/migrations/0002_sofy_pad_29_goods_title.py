# Generated by Django 4.0.5 on 2022-07-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_pricing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofy_pad_29',
            name='goods_title',
            field=models.CharField(default='undefined', max_length=50),
        ),
    ]