from django.contrib import admin

from .models import Profile

# Register your models here.
admin.site.register(Profile)

admin.site.site_header = "E-Com"
admin.site.site_title = "Admin"
admin.site.index_title = "E-Com"


class Profile(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('frist_name', 'email')
    list_filter = ('first_name', 'last_name', 'email')
