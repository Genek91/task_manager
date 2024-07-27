from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task
from .search import index_task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        index_task(task)
        process_task.delay(task.id)

    def perform_update(self, serializer):
        task = serializer.save()
        index_task(task)
