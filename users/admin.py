from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'dob', 'address', 'city_id', 'job_title', 'start_date')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)