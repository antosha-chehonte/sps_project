# Generated by Django 2.2.12 on 2020-05-02 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_document_doc_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='status',
        ),
    ]
