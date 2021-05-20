from rest_framework import viewsets, response, status

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
