from django.contrib import admin
from django.utils.html import  mark_safe
# Register your models here.
from .models import Category, Course, Lesson , Tag, Comment, Like
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.urls import path
from django.template.response import TemplateResponse
from . import dao  # Dấu chấm (.) để import module trong cùng thư mục

class CourseAppAdminSite (admin.AdminSite):
    site_header = 'He Thong Khoa Hoc Truc Tiep!'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view, name='course_stats')
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats_view.html', {
            'stats' : dao.count_courses_by_cate()
        })

admin_site = CourseAppAdminSite(name='myapp')

class CateAdmin (admin.ModelAdmin):
    list_display = ['pk','name']
class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Course
        fields = '__all__'
class TagInlineAdmin (admin.StackedInline):
    model = Course.tags.through
class CourseAdmin (admin.ModelAdmin):
    readonly_fields = ['img']  # Đặt tên phương thức dạng chuỗi
    form = CourseForm
    inlines = [TagInlineAdmin]
    def img(self,Course):
        if Course :
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=Course.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin_site.register(Category, CateAdmin)
admin_site.register(Course,CourseAdmin)
admin_site.register(Lesson)
admin_site.register(Comment)
admin_site.register(Like)


