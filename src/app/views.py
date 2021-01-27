from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Data


class HomePageView(ListView):

    model = Data
    template_name = 'app/index.html'
    context_object_name = 'list'


class CardDetailView(LoginRequiredMixin, DetailView):
    
    model = Data
    login_url = 'account_login'
    template_name = 'app/card_detail.html'


class BlogUpdateView(UpdateView): 

    model = Data
    template_name = 'app/post_edit.html'
    fields = ['group', 'text']


class BlogDeleteView(DeleteView): 

    model = Data
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('home')