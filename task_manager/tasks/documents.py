from elasticsearch_dsl import Document, field
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
from .models import Task

connections.configure(
    default={'hosts': 'localhost'},
    dev={
        'hosts': ['localhost:9200'],
        'sniff_on_start': True
    }
)


class TaskDocument(Document):
    title = field.Text()
    description = field.Text()

    class Index:
        name = 'tasks'

    class Django:
        model = Task


registry.register_document(TaskDocument)
