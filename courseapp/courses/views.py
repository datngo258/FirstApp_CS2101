from django.shortcuts import render
from rest_framework import viewsets, generics, status,parsers, permissions
from rest_framework.response import Response
from .models import Category , Course, Lesson,User, Comment, Like

from rest_framework.decorators import  action
from . import serializers, paginators, perms

# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView) :
    queryset = Category.objects.all()
    serializer_class =  serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CoursesSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q :
            queries = queries.filter(subject__icontains=q)
        return  queries

    @action(methods=['get'], detail=True)
    def lessons(self, request, pk):
        course = self.get_object()
        lessons = course.lesson_set.filter(active=True).all()

        return Response(serializers.LessonSerializer(lessons, context={'request': request}, many=True).data,
                        status=status.HTTP_200_OK)

class LessonViewSet (viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonDetailSerializer
    permission_classes = [permissions.AllowAny()]
    def get_permissions(self):
            if self.action in ['add_comment','like']:
                return [permissions.IsAuthenticated()]
            return self.permission_classes

    @action(methods=['post'], url_path="comment", detail=True )
    def add_comment(self, request, pk  ):
        c = Comment.objects.create(user = request.user , lesson = self.get_object(), content =request.data.get('content'))
        return Response(serializers.CommentSerializer(c).data,status = status.HTTP_201_CREATED)
    @action(methods=['post'], url_path="like", detail=True )
    def like (self, request, pk):
        like, created =Like.objects.get_or_create(user=request.user, lesson = self.get_object())
        if not created :
            like.active = not like.active
            like.save()
        return Response(serializers.LessonDetailSerializer(self.get_object(),context={'request' : request}).data
            ,status=status.HTTP_200_OK)
class CommentViewSet(viewsets.ViewSet,generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [perms.OwnerAuthenticated]
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='current-user', detail=False)
    def get_current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)