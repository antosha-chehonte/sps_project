from django.forms import ModelForm
from .models import Document, DocVersion


class DocForm(ModelForm):
    class Meta:
        model = Document
        fields = (
            'date_issue',
            'doc_number',
            'doc_title',
            'position',
            'rank',
            'fullname',
            'place_issue',
            'doc_type',
            'doc_status',
        )
