from .models import Category, Course
from rest_framework import  serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields ='__all__'


class CoursesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, course):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri('/static/%s' % course.image.name)
        return '/static/%s' % course.image.name

    class Meta:
        model = Course
        fields = '__all__'  # Đảm bảo chứa 'image'