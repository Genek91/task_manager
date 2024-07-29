from rest_framework import viewsets

from api.models import Task
from api.serializers import TaskSerializer
from task_manager.tasks import simple_task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        simple_task.delay()
        return super().create(request, *args, **kwargs)
