# Generated by Django 2.2.12 on 2020-04-24 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200425_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='change',
        ),
    ]
