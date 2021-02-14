from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PaginationDemo

class PaginationDemoList(LoginRequiredMixin, ListView):
    model = PaginationDemo
    # login_url = '/api-auth/login/'
    paginate_by = 10
    # ordering = ['name']

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'amount')

        # validate ordering
        if ordering not in ('name', 'amount', '-name', '-amount', ):
            ordering = 'amount'
        
        return ordering

class PaginationDemoDetail(LoginRequiredMixin, DetailView):
    model = PaginationDemo
    login_url = '/api-auth/login/'
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = PaginationDemo.objects.get(uuId=pk)
        return obj
