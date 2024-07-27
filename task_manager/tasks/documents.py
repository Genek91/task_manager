from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

connections.create_connection()
connections.configure(
    default={'hosts': 'localhost:9200'}
)


class TaskDocument(Document):
    title = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'tasks'


TaskDocument.init()
