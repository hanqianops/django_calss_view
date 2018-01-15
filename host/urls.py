from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'host-detail/(?P<pk>\d+)/$', views.HostDetailView.as_view(), name="host-detail"),
    url(r'host-create/$', views.HostCreateView.as_view(), name="host-create"),
    url(r'host-edit/(?P<pk>\d+)/$', views.HostEditView.as_view(), name="host-edit"),
    url(r'host-delete/(?P<pk>\d+)/$', views.HostDeleteView.as_view(), name="host-delete"),
    url(r'^$', views.HostListView.as_view(), name="host-list"),

]