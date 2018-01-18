# Generated by Django 2.0 on 2018-01-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecarousel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='homefeatured',
            name='id',
        ),
        migrations.AlterField(
            model_name='homecarousel',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='homefeatured',
            name='product_one',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='homefeatured',
            name='product_three',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='product_three', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='homefeatured',
            name='product_two',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='product_two', to='products.Category'),
        ),
    ]
