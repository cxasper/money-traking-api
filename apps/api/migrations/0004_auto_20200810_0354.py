# Generated by Django 3.0.8 on 2020-08-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200810_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
