from django.db import models
from django.urls import reverse


class Place(models.Model):
    place_issue = models.CharField(
        max_length=30,
        verbose_name="Место издания",
        help_text="Место издания"
    )

    def __str__(self):
        return self.place_issue

    class Meta:
        ordering = ('place_issue',)
        verbose_name = "Место издания документа"
        verbose_name_plural = "Места издания документов"


class DocStatus(models.Model):
    doc_status = models.CharField(
        max_length=30,
        verbose_name="Статус документа",
        help_text="Сведения о текущем статусе документа"
    )

    def __str__(self):
        return self.doc_status

    class Meta:
        # ordering = ('doc_status',)
        verbose_name = "Статус документа"
        verbose_name_plural = "Сведения о текущем статусе документа"


class DocType(models.Model):
    doc_type = models.CharField(
        max_length=30,
        verbose_name="Тип документа",
        help_text="Тип документа"
    )
    doc_imperative = models.CharField(
        max_length=30,
        verbose_name="Императив документа",
        help_text="Императив документа"
    )

    def __str__(self):
        return self.doc_type

    class Meta:
        ordering = ('doc_type',)
        verbose_name = "Тип документа"
        verbose_name_plural = "Типы документов"


# todo: предусмотреть хранение изменяющего документа
'''
Изменяющий документ хранить в основной модели документов:
Предусмотреть у основного документа статус "Изменяющий".
Приоритет поиска организовать с учетом статуса.
'''


class Document(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID документа")
    date_issue = models.DateField(verbose_name="Дата издания", help_text="Дата издания")
    doc_number = models.CharField(max_length=30, verbose_name="Номер документа", help_text="Номер документа")
    doc_title = models.TextField(verbose_name="Название", help_text="Название документа")
    position = models.CharField(max_length=40, verbose_name="Должность", help_text="Должность")
    rank = models.CharField(max_length=50, blank=True, verbose_name="Классный чин",
                            help_text="Классный чин должностного лица")
    fullname = models.CharField(max_length=30, verbose_name="Имя", help_text="Инициалы и фамилия должностного лица")
    # change = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    place_issue = models.ForeignKey(
        Place, verbose_name="Место издания",
        help_text="Место издания документа",
        on_delete=models.PROTECT
    )

    doc_type = models.ForeignKey(
        DocType,
        verbose_name="Тип документа",
        help_text="Тип документа",
        on_delete=models.PROTECT
    )

    doc_status = models.ForeignKey(
        DocStatus,
        verbose_name="Статус документа",
        help_text="Сведения о текущем статусе документа",
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ('-date_issue',)
        verbose_name = "Основной документ"
        verbose_name_plural = "Основные документы"

    def __str__(self):
        return '%s от %s №%s' % (self.doc_type, self.date_issue, self.doc_number)

    def get_absolute_url(self):
        return reverse('document', args=(self.pk,))


class Control(models.Model):
    control_date = models.DateField(
        verbose_name="Контрольные даты",
        help_text="Контрольные даты",
        null=True
    )
    control_officer = models.CharField(
        max_length=40,
        verbose_name="Корреспондент контроля",
        help_text="Корреспондент контроля",
        null=True
    )

    control_doc = models.ForeignKey(
        Document,
        verbose_name="Контрольный документ",
        help_text="Контрольный документ",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.control_doc

    class Meta:
        ordering = ('control_date',)
        verbose_name = "Контрольная дата"
        verbose_name_plural = "Контрольные даты"


class DocVersion(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    date_version = models.DateField(verbose_name="Дата редакции", help_text="Дата редакции")
    date_start = models.DateField(verbose_name="Начало действия редакции", help_text="Начало действия редакции")
    preamble = models.TextField(blank=True, verbose_name="Преамбула", help_text="Преамбула документа")
    text = models.TextField(verbose_name="Текст документа", help_text="Текст документа")

    class Meta:
        ordering = ('-date_start',)
        verbose_name = "Версия документа"
        verbose_name_plural = "Версии документов"

    def __str__(self):
        return '%s от %s №%s (ред. от %s)' % \
               (self.document.doc_type,
                self.document.date_issue,
                self.document.doc_number,
                self.date_version
                )

    # def get_absolute_url(self):
    #     return reverse('catalog_docversion_detail', args=(self.pk,))


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование направления работы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'
        ordering = ['title']
