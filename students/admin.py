from django.contrib import admin
from students.models import StudentsModel

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['rollo','name','course','fee']
    # readonly_fields=['name']
    list_display_links=['rollo']
    list_editable=['course','fee']

admin.site.register(StudentsModel,StudentModelAdmin)
