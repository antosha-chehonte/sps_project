from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # индекс
    url(r'^$', views.index, name='index'),

    # urls на основе функций
    url(r'^documents/$', views.document_list, name='docs_list'),  # список документов
    path('document/<int:pk>', views.document, name='document'),  # конкретный документ
    url('document/(?P<pk>[0-9])/(?P<doc_version_id>[0-9])', views.document, name='document_version'),
    url(r'^addnew/$', views.document_add, name='document_add'),   # добавление документа
    url(r'^test/(?P<pk>[0-9])/(?P<doc_version_last_id>[0-9])/$', views.test, name='test'),   # тестовый шаблон
    url(r'^search/$', views.search, name='search'),   # поиск
    path('news/', views.news, name='news'),   # новости
    path('news/category/<int:category_id>', views.news, name='news_category'),   # новости категории
    path('news/<int:news_id>', views.news_view, name='news_view'),   # конкретная новость
 ]



