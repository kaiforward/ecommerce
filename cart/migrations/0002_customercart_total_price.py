# Generated by Django 2.0 on 2018-01-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercart',
            name='total_price',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
