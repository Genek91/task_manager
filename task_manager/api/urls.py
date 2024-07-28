from django.urls import path, include
from rest_framework import routers

from api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
