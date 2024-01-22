from django.contrib import admin
from .models import Profile, Record, ImagesRecord


# Register your models here.

class ImagesInLine(admin.TabularInline):
    model = ImagesRecord



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'tel']

    def get_username(self, obj):
        return obj.user.username


class RecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'title']
    search_fields = ['title']
    list_filter = ['created_at']
    inlines = [ImagesInLine]

admin.site.register(Record, RecordAdmin)
admin.site.register(Profile, ProfileAdmin)