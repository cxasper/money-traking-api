# Generated by Django 3.0.8 on 2020-08-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200728_0338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='display_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='name',
        ),
    ]
