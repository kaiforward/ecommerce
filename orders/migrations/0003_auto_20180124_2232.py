# Generated by Django 2.0 on 2018-01-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_customerorder_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerorder',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AddField(
            model_name='customerorder',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
