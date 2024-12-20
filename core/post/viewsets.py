from rest_framework.permissions import IsAuthenticated
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.decorators import action

class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if view.basename in ["post"]:
            return bool(request.user and
            request.user.is_authenticated)
        return False
    def has_permission(self, request, view):
        if view.basename in ["post"]:
            if request.user.is_anonymous:
              return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False
        

class PostViewSet(AbstractViewSet):
        http_method_names = ('post', 'get', 'put', 'delete')
        permission_classes = (IsAuthenticated,)
        serializer_class = PostSerializer

        def get_queryset(self):
         return Post.objects.all()
        
        def get_object(self):
            obj = Post.objects.get_object_by_public_id(
            self.kwargs['pk'])
            self.check_object_permissions(self.request, obj)
            return obj
        
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        @action(methods=['post'], detail=True)
        def like(self, request, *args, **kwargs):
            post = self.get_object()
            user = self.request.user

            user.like(post)

            serializer = self.serializer_class(post)

            return Response(serializer.data, status=status.HTTP_200_OK)

        @action(methods=['post'], detail=True)
        def remove_like(self, request, *args, **kwargs):
            post = self.get_object()
            user = self.request.user

            user.remove_like(post)

            serializer = self.serializer_class(post)

            return Response(serializer.data, status=status.HTTP_200_OK)