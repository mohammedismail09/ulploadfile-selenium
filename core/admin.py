from django.contrib import admin
from .models import UploadedFile
from django.utils.html import format_html

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file_link', 'file_format')

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" download>Download</a>', obj.file.url)
        return "-"
    file_link.short_description = 'File'

    def file_format(self, obj):
        if obj.file:
            return obj.file.name.split('.')[-1]
        return "-"
    file_format.short_description = 'Format'

admin.site.register(UploadedFile, UploadedFileAdmin)
