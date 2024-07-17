from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)

# Customize Admin Site
class MyAdminSite(AdminSite):
    site_header = 'Mindmaster Administration'
    site_title = 'Mindmaster Admin'
    index_title = 'Welcome to Mindmaster Admin'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(UploadedFile, UploadedFileAdmin)
