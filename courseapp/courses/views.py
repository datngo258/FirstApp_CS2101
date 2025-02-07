from django.shortcuts import render
from  rest_framework import viewsets , generics
from .models import Category , Course

from . import serializers, paginators
# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView) :
    queryset = Category.objects.all()
    serializer_class =  serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView) :
    queryset = Course.objects.filter(active=True).all()
    serializer_class =  serializers.CoursesSerializer
    serializer_class =paginators.CoursePaginator