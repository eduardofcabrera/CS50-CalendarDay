from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class Priority():

    priorityChoises = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Very high'),
    ]


class DayWeek(models.Model):
    
    days = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    day = models.PositiveIntegerField(choices=days, blank=False)


class RoutineContent(models.Model):

    content = models.TextField(blank=False, max_length=216, verbose_name="content", serialize=True)
    priority = models.PositiveIntegerField(choices=Priority.priorityChoises, blank=True, serialize=True, null=True)
    date_created = models.DateTimeField(default=now, verbose_name='date created')
    date_finish = models.DateTimeField(verbose_name='date finish', serialize=True, blank=True, null=True)
    day_week = models.ManyToManyField(DayWeek, blank=True)
    is_routine = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def serialize(self):
        return {
            "id": self.pk,
            "content": self.content,
            "priority": self.priority,
            "date_created": self.date_created,
            "date_finish": self.date_finish,
            "day_week": self.day_week,
            "is_routine": self.is_routine,
        }


class Advice(models.Model):
    
    type_TAA = models.CharField(max_length=25, default='Advice')
    routine_content = models.ForeignKey(RoutineContent, on_delete=models.CASCADE, blank=False)

class Appointment(models.Model):
    
    type_TAA = models.CharField(max_length=25, default='Appointment')
    routine_content = models.ForeignKey(RoutineContent, on_delete=models.CASCADE, blank=False)

class Task(models.Model):

    type_TAA = models.CharField(max_length=25, default='Task')
    routine_content = models.ForeignKey(RoutineContent, on_delete=models.CASCADE, blank=False)

class Routine(models.Model):
    
    routine_tasks = models.ManyToManyField(Task, blank=True)
    routine_appointments = models.ManyToManyField(Appointment, blank=True)
    routine_advices = models.ManyToManyField(Advice, blank=True)

class User(AbstractUser):
    
    user_routine = models.ForeignKey(Routine, on_delete=models.CASCADE, blank=True, null=True, related_name='owner')
    