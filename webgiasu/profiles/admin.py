'''from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()

@admin.register(User)



class ProfileUserAdmin(UserAdmin):
    list_display = ('full_name', 'email', 'years_of_birth')
    search_fields = ('full_name', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
'''



from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','full_name',)
    search_fields = ('full_name', )


# Register your models here.
admin.site.register(User, UserAdmin)


