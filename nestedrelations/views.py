from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View

from .models import Parent
from .forms import ChildACreateForm

class ParentDetailView(View):

    def get(self, request, parent_id):
        parent = get_object_or_404(Parent, id=parent_id)
        context = {'parent_id': parent_id, 'parent': parent}
        return render(request, 'nestedrelations/ParentDetail.html', context)


class ChildACreateView(View):

    def get(self, request, parent_id):
        form = ChildACreateForm(initial={'parent': parent_id})
        context = {'form': form}
        return render(request, 'nestedrelations/ChildACreate.html', context)

    def post(self, request, parent_id):
        post_data = request.POST.copy()
        post_data['parent'] = parent_id
        form = ChildACreateForm(post_data)
        if form.is_valid():
            form.save()
            return redirect(reverse('ParentDetailView', args=(parent_id, )))
        context = {'form': form}
        return render(request, 'nestedrelations/ChildACreate.html', context)
