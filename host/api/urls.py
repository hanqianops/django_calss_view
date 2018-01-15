# coding: utf-8
__author__ = "HanQian"
from django.conf.urls import url
from . import views

urlpatterns = [

    # 获取课程列表
    url(r'^host/$', views.HostInfoListView.as_view(), name='subject_list'),

    # 获取课程的详细内容
    url(r'^host/(?P<pk>\d+)/$', views.HostInfoDetailView.as_view(), name='subject_detail'),

    # 给当前的用户报名课程
    # url(r'^courses/(?P<pk>\d+)/enroll/$', views.CourseEnrollView.as_view(), name='course_enroll'),
]