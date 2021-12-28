from home.models import ContactMessage
from django.contrib import admin


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message', 'create_at']
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'create_at')


admin.site.register(ContactMessage, ContactMessageAdmin)
