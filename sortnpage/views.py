from django.views.generic import ListView, DetailView
from .models import PaginationDemo

class PaginationDemoList(ListView):
    model = PaginationDemo
    paginate_by = 5
    # ordering = ['name']

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'amount')

        # validate ordering
        if ordering not in ('name', 'amount', '-name', '-amount', ):
            ordering = 'amount'
        
        return ordering

class PaginationDemoDetail(DetailView):
    model = PaginationDemo
