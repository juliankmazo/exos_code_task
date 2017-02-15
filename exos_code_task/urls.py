"""
exos_code_task
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import IndexView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, user_list_csv_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^users/update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name='user-update'),
    url(r'^users/delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(), name='user-delete'),
    url(r'^users/create/$', UserCreateView.as_view(), name='user-create'),
    url(r'^users/download-csv', user_list_csv_view, name='user-list-csv'),
    url(r'^', IndexView.as_view(), name='user-list')
]
