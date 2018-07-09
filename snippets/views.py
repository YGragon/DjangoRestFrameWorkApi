from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

# @permission_classes((permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated, ))
permission_classes((IsAuthenticated,permissions.IsAuthenticatedOrReadOnly, ))
class SnippetList(generics.ListCreateAPIView):
    # mixins.CreateModelMixin 可以保存数据
    # generics.GenericAPIView 继承了APIView
    """
    # 这里是SnippetList接口描述
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# @permission_classes((permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated, ))
permission_classes((permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,IsAuthenticated, ))
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    读取, 更新 or 删除一个代码片段(snippet)实例(instance).
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer