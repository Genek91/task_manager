from elasticsearch_dsl import Document, Text, connections

connections.create_connection(hosts=['https://localhost:9200'])


class TaskIndex(Document):
    title = Text()
    description = Text()

    class Index:
        name = 'tasks'


def index_task(task):
    obj = TaskIndex(
        meta={'id': task.id}, title=task.title, description=task.description
    )
    obj.save()


def search_tasks(query):
    search = TaskIndex.search().query(
        "multi_match", query=query, fields=['title', 'description']
    )
    response = search.execute()
    return response
