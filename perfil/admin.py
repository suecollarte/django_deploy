from django.contrib import admin

#models
from .models import Project

# Register your models here.
#admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','des','creacion')
    list_editable = ('title','des')
    list_filter = ('title',)
    search_fields =('title',)
