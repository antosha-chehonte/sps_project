from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse
from .models import Document, DocVersion, DocType, News, Category


def test(request,
         pk,
         doc_version_last_id
         ):
    pk = pk
    doc_version_last_id = doc_version_last_id

    return render(
        request,
        'catalog/test.html',
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
        'catalog/index.html',
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
        'catalog/document_detail.html',
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
        return render(request, 'catalog/document_add.html')
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


def document_list(request, search_query=None):

    if search_query:
        doc_list = Document.objects.filter(doc_type__icontains=search_query).order_by('-date_issue')
    else:
        doc_list = Document.objects.all().order_by('-date_issue')
        # todo: получить сведения о статусе документа, преобразовать их в имя статуса из переменной DOC_STATUS
        # status_list = dict(d='Действующий', n='Недействующий', с='Изменяющий')

    doc_status = 'status'

    return render(
        request,
        'catalog/documents_list.html',
        context={'doc_list': doc_list, 'doc_status': doc_status},
    )


def search(request):

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        docs = Document.objects.filter(doc_type=q)
        return render_to_response('catalog/search_result.html',
                                  {'doc_list': docs, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def news(request):
    news_list = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news_list': news_list,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='news/news.html', context=context)


def get_category(request, category_id):
    news_list = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news_list': news_list,
        'title': 'Список новостей',
        'categories': categories,
        'category': category,
    }
    return render(request, template_name='news/news_category.html', context=context)
