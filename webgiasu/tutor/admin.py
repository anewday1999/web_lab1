# Register your models here.
from django.contrib import admin
from django.db import models
from tutor.models import findtutorpost

class UserAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    search_fields = ('title', )


# Register your models here.
admin.site.register(findtutorpost, UserAdmin)