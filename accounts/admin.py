from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import GuestEmail
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#     form = UserAdminChangeForm #edit view
#     add_form = UserAdminCreationForm # create view
#
#     # class Meta:
#     #     model = User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone',)}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = GuestEmail

admin.site.register(GuestEmail)
