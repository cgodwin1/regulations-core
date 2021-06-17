from django.contrib import admin

# Register your models here.

from .models import (
    SupplementaryContent,
    Category,
    RegulationSection,
)

class SectionsInline(admin.TabularInline):
    model = RegulationSection.supplementary_content.through

@admin.register(SupplementaryContent)
class SupplementaryContentAdmin(admin.ModelAdmin):
    inlines = [
        SectionsInline,
    ]

#admin.site.register(SupplementaryContentAdmin)
admin.site.register(Category)
admin.site.register(RegulationSection)
