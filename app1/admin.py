from django.contrib import admin
from .models import *


class DailyAttendanceAdmin(admin.ModelAdmin):
    readonly_fields = ('in_time', 'out_time')   

# Register your models here.
admin.site.register(Company)
admin.site.register(DailyAttendance, DailyAttendanceAdmin)
admin.site.register(Employee)