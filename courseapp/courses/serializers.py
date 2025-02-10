from .models import Category, Course, Lesson
from rest_framework import  serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields ='__all__'

class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, course):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri('/static/%s' % course.image.name)
        return '/static/%s' % course.image.name


class CoursesSerializer(BaseSerializer):

    class Meta:
        model = Course
        fields = '__all__'  # Đảm bảo chứa 'image'


class LessonSerializer(BaseSerializer):  # Đổi từ lesssonSerializer thành LessonSerializer
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'tags']