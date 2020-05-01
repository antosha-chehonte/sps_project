from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Max
from .models import Document, DocVersion, DocType
from .forms import DocForm


def test(request,
         pk,
         doc_version_last_id
         ):
    pk = pk
    doc_version_last_id = doc_version_last_id

    return render(
        request,
        'test.html',
        context=dict(
            pk=pk,
            doc_version_last_id=doc_version_last_id
        ),
    )


def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_docs = Document.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_docs': num_docs},
    )


def document(request,
             pk,
             doc_version_id=None,
             ):
    doc = get_object_or_404(Document, pk=pk)  # получаем все основные реквизиты документа по ключу pk
    """ 
    далее работаем с моделью DocVersion: 
    получаем список всех версиий документа (document_id=pk),
    который становится источником данных в представлении, а в шаблоне этот список итерируем в блоке ссылок на версии
    """
    doc_versions_all = DocVersion.objects.order_by('-date_version').filter(document_id=pk)
    doc_versions_count = int(doc_versions_all.count())
    doc_actual_version_id = int(doc_versions_all.first().id)  # получаем id последней редакции

    if doc_version_id:
        doc_version_id = int(doc_version_id)
        doc_version = doc_versions_all.get(id=doc_version_id)  # получаем все данные последней редакции
    else:
        doc_version = doc_versions_all.get(id=doc_actual_version_id)  # получаем все данные последней редакции
        doc_version_id = int(doc_actual_version_id)

    doc_type_id = int(doc.doc_type_id)
    doc_type = DocType.objects.get(id=doc_type_id)
    doc_type_imperative = doc_type.doc_imperative

    test_var = None

    return render(
        request,
        'document.html',
        context=dict(document=doc,
                     doc_versions_all=doc_versions_all,
                     doc_version=doc_version,
                     imperative=doc_type_imperative,
                     doc_actual_version_id=doc_actual_version_id,
                     doc_versions_count=doc_versions_count,
                     test=test_var,
                     pk=pk,
                     doc_version_id=doc_version_id
                     ),
    )


def document_add(request):
    if request.method == 'GET':
        return render(request, 'document_add.html')
    else:
        date_issue = request.POST['date_issue'],
        doc_number = request.POST['doc_number'],
        doc_title = request.POST['doc_title'],
        position = request.POST['position'],
        rank = request.POST['rank'],
        fullname = request.POST['fullname'],
        place_issue = request.POST['place_issue'],
        doc_type = request.POST['doc_type'],
        status = request.POST['status'],

        Document(
            date_issue=date_issue,
            doc_number=doc_number,
            doc_title=doc_title,
            # preamble=preamble,
            position=position,
            rank=rank,
            fullname=fullname,
            place_issue=place_issue,
            doc_type=doc_type,
            status=status,
        ).save()
        return redirect('/documents')


def document_list(request):
    doc_list = Document.objects.all().order_by('-date_issue')
    # todo: получить сведения о статусе документа, преобразовать их в имя статуса из переменной DOC_STATUS
    doc_status = "status"

    return render(
        request,
        'docs_list.html',
        context={'doc_list': doc_list, 'doc_status': doc_status},
    )


class DocumentListView(generic.ListView):
    model = Document
    paginate_by = 10


class DocCreateView(CreateView):
    template_name = 'catalog/document_create.html'
    form_class = DocForm
    success_url = reverse_lazy('docs')


class DocumentDetailView(generic.DetailView):
    model = Document

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['text'] = context['object'].docversion_set.first().text
        context['date_start'] = context['object'].docversion_set.first().date_version
        # todo: присвоить переменной imperative значение императива из модели doctype
        # context['imperative'] = context['object'].doctype_set.first().doc_imperative
        return context

