from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from hyk.users.models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):


    #fieldsets = (("User", {"fields": ("first_name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["email", "first_name", "is_superuser"]
    search_fields = ["first_name"]


admin.site.register(Profile)