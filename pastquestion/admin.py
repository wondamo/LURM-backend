from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    
    def has_permission(self, request):
        # Use is_superuser as a condition for admin access
        return request.user.is_active and request.user.is_superuser

admin.site.register(User, UserAdmin)
admin.site.register(PastQuestion)
