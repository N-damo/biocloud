from django.contrib import admin
from . import models
# Register your models here.
class TagInline1(admin.TabularInline):
    model = models.User_project_list

class TagInline2(admin.TabularInline):
    model = models.User_analysis_list

class TagInline3(admin.TabularInline):
    model = models.Data

class UserAdmin(admin.ModelAdmin):
    inlines=[TagInline1,TagInline3]
    list_display=('name','c_time')
    search_fields=('name',)

class User_project_listAdmin(admin.ModelAdmin):
    inlines=[TagInline2]
    list_display=('name','c_time')
    search_fields=('name',)


class DataAdmin(admin.ModelAdmin):
    list_display=('batch','adapter','fq1','fq2','c_time')
    search_fields=('batch',)

admin.site.register(models.User,UserAdmin)
admin.site.register(models.User_project_list,User_project_listAdmin)
admin.site.register(models.User_analysis_list)
admin.site.register(models.Data,DataAdmin)
#admin.site.register(models.Data)