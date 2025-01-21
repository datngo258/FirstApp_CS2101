from django.contrib import admin

# Register your models here.
from .models import Category, Course

class CateAdmin (admin.ModelAdmin):
    list_display = ['pk','name']

admin.site.register(Category, CateAdmin)
admin.site.register(Course)
