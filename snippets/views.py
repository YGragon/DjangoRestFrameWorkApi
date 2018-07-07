from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


@permission_classes((IsAuthenticated, ))
class SnippetList(generics.ListCreateAPIView):
    # mixins.CreateModelMixin 可以保存数据
    # generics.GenericAPIView 继承了APIView
    """
    # 这里是SnippetList接口描述
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


@permission_classes((IsAuthenticated, ))
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    读取, 更新 or 删除一个代码片段(snippet)实例(instance).
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer