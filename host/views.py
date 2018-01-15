from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import HostInfo
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
"""
LoginRequiredMixin：复制login_required装饰器的功能。
PermissionRequiredMixin：会在用户使用视图的时候检查该用户是否有指定在permission_required属性中的权限。超级用户自动拥有所有权限。
"""

class HostMixin(LoginRequiredMixin):
    model = HostInfo
    # login_url = "/login"

class HostFieldsMixin(object):
    fields = ['hostname', 'ip', 'mem', 'cpu', 'deviceclass']

class HostListView(HostMixin, ListView):
    """
    主机列表
    """
    context_object_name = 'host_list'
    template_name = 'host/list.html'

class HostDetailView(HostMixin, DetailView):
    """
    主机详细信息
    """
    template_name = 'host/detail.html'
    pk_url_kwarg = "pk"


class HostCreateView(PermissionRequiredMixin,HostMixin,HostFieldsMixin, CreateView):
    """ 更新主机 """
    permission_required = 'host.create_host'
    login_url = '/loginpage/'
    raise_exception = True
    template_name = "host/create.html"
    success_url = reverse_lazy('host:host-list')

class HostEditView(HostMixin,HostFieldsMixin, UpdateView):
    """ 编辑主机 """
    permission_required = 'host.edis_host'
    template_name = "host/edit.html"
    success_url = reverse_lazy('host:host-list')

class HostDeleteView(HostMixin, DeleteView):
    """ 删除主机 """
    permission_required = 'host.delete_host'
    template_name = "host/delete.html"
    success_url = reverse_lazy('host:host-list')