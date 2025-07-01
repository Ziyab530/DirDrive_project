from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile,BikerApplication,SupportIssue


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)

admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import UserProfile, BikerApplication, SupportIssue

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'date_of_birth', 'created_at')
    search_fields = ('user__username', 'address', 'gender')
    list_filter = ('gender', 'created_at')


@admin.register(BikerApplication)
class BikerApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'cnic', 'phone_number', 'status', 'submitted_at', 'reviewed_at')
    search_fields = ('full_name', 'cnic', 'phone_number', 'license_number', 'vehicleNumber')
    list_filter = ('status', 'submitted_at', 'reviewed_at')


@admin.register(SupportIssue)
class SupportIssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'issue_type', 'created_at')
    search_fields = ('user__username', 'description')
    list_filter = ('issue_type', 'created_at')
