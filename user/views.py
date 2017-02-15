from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from user.models import User


class IndexView(ListView):
    """Index view class"""
    model = User
    context_object_name = 'user_list'
    template_name = 'user/index.html'

class UserDetailView(DetailView):
    """User detail view class"""
    model = User
    context_object_name = 'user'

class UserCreateView(CreateView):
    """User create view class"""
    model = User
    fields = ['username', 'password', 'date_of_birth']

class UserUpdateView(UpdateView):
    """User edit view class"""
    model = User
    context_object_name = 'user_to_edit'
    fields = ['username', 'password', 'date_of_birth']

class UserDeleteView(DeleteView):
    """User delete view class"""
    model = User
    context_object_name = 'user_to_delete'
    success_url = reverse_lazy('user-list')
