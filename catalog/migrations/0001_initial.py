# Generated by Django 2.2.12 on 2020-04-24 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(help_text='Тип документа', max_length=30, verbose_name='Тип документа')),
                ('doc_imperative', models.CharField(help_text='Императив документа', max_length=30, verbose_name='Императив документа')),
            ],
            options={
                'verbose_name': 'Тип документа',
                'verbose_name_plural': 'Типы документов',
                'ordering': ('doc_type',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(help_text='ID документа', primary_key=True, serialize=False)),
                ('date_issue', models.DateField(help_text='Дата издания', verbose_name='Дата издания')),
                ('doc_number', models.CharField(help_text='Номер документа', max_length=30, verbose_name='Номер документа')),
                ('doc_title', models.TextField(help_text='Название документа', verbose_name='Название')),
                ('position', models.CharField(help_text='Должность', max_length=40, verbose_name='Должность')),
                ('rank', models.CharField(blank=True, help_text='Классный чин должностного лица', max_length=50, verbose_name='Классный чин')),
                ('fullname', models.CharField(help_text='Инициалы и фамилия должностного лица', max_length=30, verbose_name='Имя')),
                ('status', models.CharField(choices=[('d', 'Действующий'), ('n', 'Недействующий'), ('с', 'Изменяющий')], default='d', help_text='Статус документа', max_length=1, verbose_name='Статус документа')),
                ('change', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Document')),
                ('doc_type', models.ForeignKey(help_text='Тип документа', on_delete=django.db.models.deletion.PROTECT, to='catalog.DocType', verbose_name='Тип документа')),
            ],
            options={
                'verbose_name': 'Основной документ',
                'verbose_name_plural': 'Основные документы',
                'ordering': ('-date_issue',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_issue', models.CharField(help_text='Место издания', max_length=30, verbose_name='Место издания')),
            ],
            options={
                'verbose_name': 'Место издания документа',
                'verbose_name_plural': 'Места издания документов',
                'ordering': ('place_issue',),
            },
        ),
        migrations.CreateModel(
            name='DocVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_version', models.DateField(help_text='Дата редакции', verbose_name='Дата редакции')),
                ('date_start', models.DateField(help_text='Начало действия редакции', verbose_name='Начало действия редакции')),
                ('text', models.TextField(help_text='Текст документа', verbose_name='Текст документа')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Document')),
            ],
            options={
                'verbose_name': 'Версия документа',
                'verbose_name_plural': 'Версии документов',
                'ordering': ('-date_start',),
            },
        ),
        migrations.AddField(
            model_name='document',
            name='place_issue',
            field=models.ForeignKey(help_text='Место издания документа', on_delete=django.db.models.deletion.PROTECT, to='catalog.Place', verbose_name='Место издания'),
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_date', models.DateField(help_text='Контрольные даты', null=True, verbose_name='Контрольные даты')),
                ('control_officer', models.CharField(help_text='Корреспондент контроля', max_length=40, null=True, verbose_name='Корреспондент контроля')),
                ('control_doc', models.ForeignKey(help_text='Контрольный документ', on_delete=django.db.models.deletion.CASCADE, to='catalog.Document', verbose_name='Контрольный документ')),
            ],
            options={
                'verbose_name': 'Контрольная дата',
                'verbose_name_plural': 'Контрольные даты',
                'ordering': ('control_date',),
            },
        ),
    ]
