# coding: utf-8
__author__ = "HanQian"

from  rest_framework import generics
from ..models import HostInfo
from .serializers import HostInfoSerializer
from rest_framework.authentication import BasicAuthentication  # 认证方式
from rest_framework.permissions import IsAuthenticated  # 权限相关

class HostInfoListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = HostInfo.objects.all()   # 基础查询集,用来取对象
    serializer_class = HostInfoSerializer  # 用来序列化对象

class HostInfoDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = HostInfo.objects.all()
    serializer_class = HostInfoSerializer


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication  # 认证方式
from rest_framework.permissions import IsAuthenticated  # 权限相关


class CourseEnrollView(APIView):
    """
    APIView类基于Django的View类构建API功能。
    APIView类与View在使用REST Framework的定制Request以及Response对象时不同
    并且操作APIException例外的返回合适的HTTP响应。
    它还有一个内建的验证和认证系统去管理视图的访问。

    执行一个POST请求去给当前用户报名一个课程
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})