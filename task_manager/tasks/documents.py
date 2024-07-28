from .models import Task

from django_elasticsearch_dsl import Document, Index

task_index = Index('tasks')
task_index.settings(
    number_of_shard=1,
    number_of_replicas=0,
)


@task_index.doc_type
class TaskDocument(Document):
    class Django:
        model = Task
        fields = {'id', 'title', 'description'}
