from django.shortcuts  import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Data


class HomePageView(ListView):

    # queryset = Data.objects.filter(group='one')
    model = Data
    context_object_name = 'list'
    # template_name = 'app/index.html'

    def get(self, request):
        viewset_one = Data.objects.filter(group='one')
        viewset_two = Data.objects.filter(group='two')
        viewset_three = Data.objects.filter(group='three')
        context = {
            'viewset_one' : viewset_one,
            'viewset_two' : viewset_two,
            'viewset_three' : viewset_three,
        }
        return render(request, 'app/index.html', context)



class CardDetailView(LoginRequiredMixin, DetailView):
    
    model = Data
    login_url = 'account_login'
    template_name = 'app/card_detail.html'


class BlogUpdateView(UpdateView): 

    model = Data
    template_name = 'app/post_edit.html'
    fields = ['text']


class BlogDeleteView(DeleteView): 

    model = Data
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('home')