# coding: utf-8
__author__ = "HanQian"

from rest_framework import serializers
from ..models import HostInfo

class HostInfoSerializer(serializers.ModelSerializer):
    """
    给Subject模型使用的序列化器
    序列化器以一种类似的方式被定义给Django的From和ModelForm类。
    """
    class Meta:
        model = HostInfo  # 要序列化的模型
        fields = '__all__'
        # fields = ('id', 'title', 'slug')   # 序列化包含的字段， 默认包含所有字段

# from ..models import Course
#
# # class CourseSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Course
# #         fields = '__all__'
#
#
# from rest_framework import serializers
# from ..models import Course, Module
#
#
# class ModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ('order', 'title', 'description')
#
#
# class CourseSerializer(serializers.ModelSerializer):
#
#     modules = ModuleSerializer(
#                     many=True,        # 表明我们正在序列化多个对象
#                     read_only=True,   # 表明这个字段是只读的并且不可以被包含在任何输入中去创建或者升级对象
#                 )
#
#     class Meta:
#         model = Course
#         fields = ('id', 'subject', 'title', 'slug', 'overview',
#                   'created', 'owner', 'modules')


