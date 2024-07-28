from django.urls import path

from search.views import SearchTasks

urlpatterns = [
    path('task/<str:query>/', SearchTasks.as_view()),
]
