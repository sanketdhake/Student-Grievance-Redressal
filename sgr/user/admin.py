from django.contrib import admin

from .models import Student, Member

# Register your models here.
admin.site.register(Student)
admin.site.register(Member)