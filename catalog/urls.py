from django.conf.urls import url
from django.urls import path
from . import views
from .views import DocCreateView


urlpatterns = [
    # индекс
    url(r'^$', views.index, name='index'),

    # urls на основе функций
    url(r'^documents/$', views.document_list, name='docs_list'),  # список документов
    path('document/<int:pk>', views.document, name='document'),  # конкретный документ
    url('document/(?P<pk>[0-9])/(?P<doc_version_id>[0-9])', views.document, name='document_version'),
    url(r'^addnew/$', views.document_add, name='document_add'),   # добавление документа
    url(r'^test/(?P<pk>[0-9])/(?P<doc_version_last_id>[0-9])/$', views.test, name='test'),   # тестовый шаблон

    # urls на основе классов
    url(r'^add/$', DocCreateView.as_view(), name='add'),  # добавление документа
    url(r'^docs/$', views.DocumentListView.as_view(), name='docs'),  # список документов
    url(r'^doc/(?P<pk>\d+)$', views.DocumentDetailView.as_view(), name='document_detail'),  # конкретный документ
 ]

