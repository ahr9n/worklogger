from django.contrib import admin
from django.db.models.aggregates import Sum
from .models import Log, Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_total_logged_hours',]
    def get_total_logged_hours(self, obj):
        result = obj.log_set.all().aggregate(total=Sum("duration"))
        return result["total"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Log)
