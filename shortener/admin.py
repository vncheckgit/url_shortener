from django.contrib import admin
from .models import URL, QRCode


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'shortened_link', 'created_at', 'click_count', 'user')
    search_fields = ('original_url', 'short_code')
    list_filter = ('created_at', 'user')
    readonly_fields = ('created_at', 'click_count', 'shortened_link')
    fieldsets = (
        (None, {
            'fields': ('original_url', 'short_code', 'shortened_link', 'user')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('click_count', 'created_at'),
        }),
    )


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at')
    readonly_fields = ('created_at', 'url', 'image')
