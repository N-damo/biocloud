from django.contrib import admin
from . import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','sex','c_time')
    search_fields=('name',)

admin.site.register(models.User,UserAdmin)