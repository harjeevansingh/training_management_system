from django.contrib import admin
from .models import Student, Training, Project, WorkUpdates


# Register your models here.
admin.site.register(Student)
admin.site.register(Training)
admin.site.register(Project)
admin.site.register(WorkUpdates)
