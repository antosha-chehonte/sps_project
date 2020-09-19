from django.contrib import admin
from .models import Document, Place, DocType, Control, DocVersion, News, Category


class DocVersionInline(admin.TabularInline):
    model = DocVersion


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_type', 'date_issue', 'doc_number', 'doc_title')
    inlines = [DocVersionInline]


admin.site.register(Place)
admin.site.register(DocType)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Control)
admin.site.register(DocVersion)
admin.site.register(News)
admin.site.register(Category)

