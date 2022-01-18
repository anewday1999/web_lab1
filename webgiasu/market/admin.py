# Register your models here.
from django.contrib import admin
from django.db import models
from market.models import marketpost

class UserAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    search_fields = ('title', )


# Register your models here.
admin.site.register(marketpost, UserAdmin)