from django.contrib import admin
<<<<<<< HEAD
from .models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')
    list_editable = ('role',)
=======
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
