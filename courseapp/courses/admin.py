from django.contrib import admin
from .models import Category, Courses, Lesson, Tags

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(Tags)