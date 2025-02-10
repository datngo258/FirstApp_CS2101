from django.shortcuts import render
from rest_framework import viewsets, generics, status,parsers, permissions
from rest_framework.response import Response
from .models import Category , Course, Lesson,User
from rest_framework.decorators import  action
from . import serializers, paginators
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
    serializer_class = serializers.LessonSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    @action(methods=['get'], url_name='current-user', detail=False )
    def current_user (self, request ):
        return Response(serializers.UserSerializer(request.user).data)
# class UserViewSet(viewsets.GenericViewSet, generics.CreateAPIView):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = serializers.UserSerializer
#     parser_classes = [parsers.MultiPartParser]
#
#     def get_permissions(self):
#         if self.action == 'current_user':  # Sửa __eq__('current_user')
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]
#
#     @action(methods=['get'], detail=False, name='current-user')
#     def current_user(self, request):
#         return Response(serializers.UserSerializer(request.user).data)
