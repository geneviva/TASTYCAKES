# Generated by Django 3.2.15 on 2022-09-29 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220928_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='house_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='pin',
        ),
    ]
