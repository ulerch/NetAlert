from django.contrib import admin
from .models import Nature, Origin, Alert, Revision


@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    pass


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    pass


class RevisionAdmin(admin.TabularInline):
    model = Revision


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    inlines = [
        RevisionAdmin,
    ]
