from django.contrib import admin
from .models import School, Professor, Course, Rating, Profile

# Register your models here.
admin.site.register(School)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Rating)
admin.site.register(Profile)