from django.contrib import admin
from .models import Poetry, Prose

@admin.register(Poetry)
class PoetryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'dynasty', 'created_at', 'updated_at')
    list_filter = ('dynasty',)
    search_fields = ('title', 'author', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'author', 'dynasty', 'type')
        }),
        ('内容信息', {
            'fields': ('content', 'translation')
        }),
        ('媒体信息', {
            'fields': ('video_url', 'cover_image')
        }),
        ('时间信息', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.type = 'poetry'  # 确保类型正确
        super().save_model(request, obj, form, change)

@admin.register(Prose)
class ProseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'dynasty', 'created_at', 'updated_at')
    list_filter = ('dynasty',)
    search_fields = ('title', 'author', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'author', 'dynasty', 'type')
        }),
        ('内容信息', {
            'fields': ('content', 'translation', 'annotation', 'appreciation')
        }),
        ('媒体信息', {
            'fields': ('video_url', 'cover_image')
        }),
        ('时间信息', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.type = 'prose'  # 确保类型正确
        super().save_model(request, obj, form, change)
