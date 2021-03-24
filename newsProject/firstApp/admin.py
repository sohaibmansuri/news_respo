from django.contrib import admin
from firstApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age']
admin.site.register(Student,StudentAdmin)
