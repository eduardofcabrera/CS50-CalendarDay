from django.contrib import admin
from .models import User, Routine, Task, Appointment, Advice, DayWeek, RoutineContent


# Register your models here.


admin.site.register(User)
admin.site.register(Task)
admin.site.register(Appointment)
admin.site.register(Advice)
admin.site.register(DayWeek)
admin.site.register(RoutineContent)
admin.site.register(Routine)