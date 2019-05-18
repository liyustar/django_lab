from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

# Create your views here.

from .forms import DictForm
from .models import Dict

class DictUpdateView(UpdateView):
    template_name = 'dicts/dict_create.html'
    #queryset = Article.objects.all()
    form_class = DictForm

    def get_object(self):
        id_ = self.kwargs.get("name")
        return get_object_or_404(Dict, pk=id_)


def dict_create(request, *args, **kwargs):
    print(request)
    form = DictForm(request.POST or None)
    print('AAAA: form create')
    if form.is_valid():
        print('BBBB: form is valid')
        form.save()

    context = {
        "form": form
    }
    return render(request, 'dicts/dict_create.html', context)

def detail(request, *args, **kwargs):
    objs = Dict.objects.all()
    return render(request, 'dicts/detail.html', {"objs": objs})