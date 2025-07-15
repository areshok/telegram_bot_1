from django.contrib import admin

# Register your models here.
from .models import Group, User
from .forms import UserFormAdmin

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "is_staff"]
    form = UserFormAdmin

@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    #list_display = ["all"]
    pass
