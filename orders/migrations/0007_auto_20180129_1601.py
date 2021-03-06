# Generated by Django 2.0 on 2018-01-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180125_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_items', to='orders.Shipping')),
            ],
        ),
        migrations.AddField(
            model_name='customerorder',
            name='shipping_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='stripe_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='country',
            field=models.CharField(max_length=200),
        ),
    ]
