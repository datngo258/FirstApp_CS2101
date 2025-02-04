from django.contrib import admin
from django.utils.html import  mark_safe
# Register your models here.
from .models import Category, Course, Lesson , Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

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


admin.site.register(Category, CateAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
