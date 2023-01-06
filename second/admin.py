from django.contrib import admin

from second.models import Lead, LeadState


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    pass


@admin.register(LeadState)
class LeadStateAdmin(admin.ModelAdmin):
    pass

