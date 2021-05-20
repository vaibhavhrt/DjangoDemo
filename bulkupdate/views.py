from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Todo


class TodoList(ListView):
    model = Todo


class TodoStatusBulkUpdate(View):
    def post(self, request):
        status = request.POST.getlist("status", [])
        objs = Todo.objects.filter(pk__in=status)
        for obj in objs:
            obj.status = 1
        Todo.objects.bulk_update(objs, ['status'])
        print(request.POST, status, objs)
        return HttpResponseRedirect(reverse('TodoListView'))
