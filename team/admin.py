from django.contrib import admin

from team.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'work', 'create_at']
    list_filter = ['name']


admin.site.register(Team, TeamAdmin)
