
from django.contrib import admin
from django.urls import path,re_path, include
import debug_toolbar
from courses.admin import admin_site  # ✅ Đúng đường dẫn
from rest_framework import  routers
from . import views


routers = routers.DefaultRouter()
routers.register('categories', views.CategoryViewSet , basename='categories' )
routers.register('courses', views.CourseViewSet , basename='courses' )
routers.register('lessons', views.LessonViewSet , basename='lessons' )
routers.register('users', views.UserViewSet , basename='users' )
routers.register('comments', views.CommentViewSet , basename='commments' )

urlpatterns = [
    path('',include(routers.urls)),
]
