from django.test import TestCase
from .models import User, Routine, RoutineContent, Task, Advice, Appointment, DayWeek
from .get import *
from datetime import datetime, timedelta
# Create your tests here.

class getsFunctionTestCase(TestCase):

    def setUp(self):

        user_a = User.objects.create_user(username='user_a', email='user_a@exp.com', password='user_a')
        content_a = RoutineContent.objects.create(content='content_a')
        task_a = Task.objects.create(routine_content=content_a)
        advice_a = Advice.objects.create(routine_content=content_a)
        appointment_a = Appointment.objects.create(routine_content=content_a)
        routine_a = Routine.objects.create()
        routine_a.routine_tasks.add(task_a)
        routine_a.routine_advices.add(advice_a)
        routine_a.routine_appointments.add(appointment_a)


    def test_getUserRoutine(self):
        user_a = User.objects.get(username='user_a')
        routine_a = Routine.objects.create()
        user_a.user_routine = routine_a
        user_a.save()
        routine = getUserRoutine(user_a)
        self.assertEqual(routine, routine_a)

    def test_getUserByUsername(self):
        user_a = User.objects.get(pk=1)
        user_a_get = getUserByUsername('user_a')
        self.assertEqual(user_a, user_a_get)

    def test_getUserByPK(self):
        user_a = User.objects.get(username='user_a')
        user_a_get = getUserByPK(1)
        self.assertEqual(user_a, user_a_get)

    def test_getUserTasks(self):
        user_a = getUserByUsername('user_a')
        content = RoutineContent.objects.create(content='content')
        task_a = Task.objects.create(routine_content=content)
        task_b = Task.objects.create(routine_content=content)
        routine_a = Routine.objects.create()
        routine_a.routine_tasks.add(task_a, task_b)
        tasks = routine_a.routine_tasks.all()
        user_a.user_routine = routine_a
        user_a.save()
        task_a_get = getUserTasks(user_a)
        tasks = list(tasks)
        task_a_get = list(task_a_get)
        self.assertEqual(tasks, task_a_get)

    def test_getUserAdvices(self):
        user_a = getUserByUsername('user_a')
        content = RoutineContent.objects.create(content='content')
        advice_a = Advice.objects.create(routine_content=content)
        routine_a = Routine.objects.create()
        routine_a.routine_advices.add(advice_a)
        advices = routine_a.routine_advices.all()
        user_a.user_routine = routine_a
        user_a.save()
        advices_get = getUserAdvices(user_a)
        advices = list(advices)
        advices_get = list(advices_get)
        self.assertEqual(advices, advices_get)

    def test_getRoutineContent(self):
        content = RoutineContent.objects.get(pk=1)
        task_a = Task.objects.get(pk=1)
        appointment_a = Appointment.objects.get(pk=1)
        advice_a = Advice.objects.get(pk=1)
        content_task = getRoutineContent(task_a)
        content_appointment = getRoutineContent(appointment_a)
        content_advice = getRoutineContent(advice_a)
        self.assertEqual(content, content_task)
        self.assertEqual(content, content_advice)
        self.assertEqual(content, content_appointment)

    def test_timeOfContent(self):
        now = datetime.now()
        finish = now + timedelta(days=2)
        content = RoutineContent.objects.create(date_finish=finish)
        task = Task.objects.create(routine_content=content)
        day_finish = getFinishDay(task)
        day_created = getCreatedDay(task)
        self.assertEquals(day_created+2, day_finish)

    def test_getDayWeek(self):
        monday = DayWeek.objects.create(day=0)
        wednesday = DayWeek.objects.create(day=2)
        content = RoutineContent.objects.create(content='content')
        content.day_week.add(monday, wednesday)
        content.save()
        array_day = [monday, wednesday]
        task = Task.objects.create(routine_content=content)
        days = getDayWeek(task)
        self.assertEquals(days, array_day)

    def test_getDateCreated(self):
        content = RoutineContent.objects.create(content='content')
        date = content.date_created
        task = Task.objects.create(routine_content=content)
        date_get = getCreatedDate(task)
        self.assertEqual(date, date_get)

    def test_getFinishDate(self):
        content = RoutineContent.objects.create(content='content')
        date = content.date_finish
        task = Task.objects.create(routine_content=content)
        date_get = getFinishDate(task)
        self.assertEqual(date, date_get)

    def test_getContent(self):
        content = RoutineContent.objects.create(content='content')
        content_content = content.content
        task = Task.objects.create(routine_content=content)
        content_get = getContent(task)
        self.assertEqual(content_content, content_get)

    def test_getPriority(self):
        content = RoutineContent.objects.create(content='content', priority=1)
        priority = content.priority
        task = Task.objects.create(routine_content=content)
        priority_get = getPriority(task)
        self.assertEquals(priority, priority_get)

    def test_getIsRoutine(self):
        content = RoutineContent.objects.create(content='content', is_routine=True)
        is_routine = content.is_routine
        task = Task.objects.create(routine_content=content)
        is_routine_get = getIsRoutine(task)
        self.assertEquals(is_routine, is_routine_get)

    def test_getPlace(self):
        content = RoutineContent.objects.create(content='content')
        appointment = Appointment.objects.create(routine_content=content, place='Rue')
        place = appointment.place
        place_get = getPlace(appointment)
        self.assertEquals(place, place_get)

    def test_getActive(self):
        content = RoutineContent.objects.create(content='content')
        advice = Advice.objects.create(routine_content=content, active=True)
        active_get = getActive(advice)
        self.assertTrue(active_get)

    def test_getFinished(self):
        content = RoutineContent.objects.create(content='content')
        task = Task.objects.create(routine_content=content)
        finished_get = getFinished(task)
        self.assertFalse(finished_get)


        