from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from api.serializers import TaskSerializer
from api.documents import TaskDocument


class SearchTasks(APIView, LimitOffsetPagination):

    def get(self, request, query):
        try:
            q = Q(
                'multi_match', query=query,
                fields=[
                    'title',
                    'description',
                ], fuzziness='auto')
            search = TaskDocument.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = TaskSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as exc:
            return HttpResponse(exc, status=500)
