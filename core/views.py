import csv
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core.models import User
from core.templatetags.user_tags import is_user_allowed, bizz_fuzz


class IndexView(ListView):
    """Index view class"""
    model = User
    context_object_name = 'user_list'


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


def user_list_csv_view(response):
    """Return a csv file listing all users"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exos_users.csv"'

    users = User.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Elegible', 'Random Number', 'BizzFuzz'])
    for user in users:
        writer.writerow([
            user.username,
            user.date_of_birth,
            is_user_allowed(user.date_of_birth),
            user.random_number,
            bizz_fuzz(user.random_number)
        ])
    return response
