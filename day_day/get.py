from .models import User, Routine, RoutineContent, Task, Advice, Appointment, DayWeek
from datetime import datetime, date 
from math import floor

def getUserByRequest(request):
    return request.user

def getUserByUsername(username):
    return User.objects.get(username=username)

def getUserByPK(pk):
    return User.objects.get(pk=pk)

def getUserRoutine(user):
    routine = Routine.objects.filter(owner=user).first()
    return routine

def getAllTasks():
    return Task.objects.all()

def getAllAdvices():
    return Advice.objects.all()

def getAllAppoitments():
    return Appointment.objects.all()

def getUserTasks(user):
    routine = user.user_routine
    tasks = routine.routine_tasks.all()
    return tasks

def getUserAdvices(user):
    routine = user.user_routine
    advices = routine.routine_advices.all()
    return advices

def getUserAppointments(user):
    routine = user.user_routine
    appointments = routine.routine_appointments.all()
    return appointments

def getRoutineContent(object_TAA):
    routine_content = object_TAA.routine_content
    return routine_content

def getTaskByPK(pk):
    return Task.objects.get(pk=pk)

def getAppointmentByPK(pk):
    return Appointment.objects.get(pk=pk)

def getAdviceByPK(pk):
    return Advice.objects.get(pk=pk)

def getCreatedDay(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    day = routine_content.date_created
    day = day.weekday()
    return day

def getFinishDay(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    day = routine_content.date_finish
    day = day.weekday()
    return day

def getDayWeek(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    days = routine_content.day_week.all()
    return list(days)

def getCreatedDate(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    date_created = routine_content.date_created
    return date_created

def getFinishDate(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    date_finish = routine_content.date_finish
    return date_finish

def getContent(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    content = routine_content.content
    return content

def getPriority(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    priority = routine_content.priority
    return priority

def getIsRoutine(object_TAA):
    routine_content = getRoutineContent(object_TAA)
    is_routine = routine_content.is_routine
    return is_routine

def getActive(object_TAA):
    active = object_TAA.active
    return active

def getDateByDjangoDate(date, tiemzone=0):
    
    date_string = date.strftime("%d/%m/%y (%H:%M)")
    return date_string


def getRows(request):

    objects_TAA = getAllDaysObjects(request)
    numberOfTAARows = getNumberOfTAARows(objects_TAA)
    rows = getRowsTAA(objects_TAA, numberOfTAARows)

    return rows


def getNumberOfTAARows(objects):
    
    numberOfTAARows = {}

    for object_TAA in objects:
        numberOfRows = getNumberOfRows(object_TAA, objects)
        numberOfTAARows[object_TAA] = numberOfRows

    return numberOfTAARows

def getNumberOfRows(object_TAA, objects):

    numberOfObjects =  len(objects[object_TAA])
    numberOfRows = floor(numberOfObjects / 3) + 1
    return numberOfRows

def getAllDaysObjects(request):

    user = getUserByRequest(request)
    objects_TAA = getAllDaysObjectsByUser(user)

    return objects_TAA

def getAllDaysObjectsByUser(user):

    day = date.today()
    day_string = day.strftime("%d/%m/%Y")
    objects_TAA = getObjectsOfAllDays(user, day_string)

    return objects_TAA

def getObjectsOfAllDays(user, day_string):

    tasks = getTasksOfAllDays(user, day_string)
    advices = getAdvicesOfAllDays(user, day_string)
    appointments = getAppointmentsOfAllDays(user, day_string)

    objectsOfAllDays = sortObjectsByDate(tasks, advices, appointments)

    return objectsOfAllDays

def getTasksOfAllDays(user, day_string):

    tasks = getUserTasks(user)
    tasks_off_all_days = objectsOfAllDays(tasks, day_string)

    return tasks_off_all_days

def getAdvicesOfAllDays(user, day_string):

    advices = getUserAdvices(user)
    advices_of_all_days = objectsOfAllDays(advices, day_string)

    return advices_of_all_days

def getAppointmentsOfAllDays(user, day_string):

    appointments = getUserAppointments(user)
    appointments_of_all_days = objectsOfAllDays(appointments, day_string)

    return appointments_of_all_days

def objectsOfAllDays(objects_TAA, day_string):

    allDaysObjects = {
        'day': [],
        'week': [],
        'month': []
    }

    for object_TAA in objects_TAA:
        if isTheSameDay(object_TAA, day_string):
            allDaysObjects['day'].append(object_TAA)
            allDaysObjects['week'].append(object_TAA)
            allDaysObjects['month'].append(object_TAA)
        elif isTheSameWeek(object_TAA, day_string):
            allDaysObjects['week'].append(object_TAA)
            allDaysObjects['month'].append(object_TAA)
        elif isTheSameMonth(object_TAA, day_string):
            allDaysObjects['month'].append(object_TAA)
        
    return allDaysObjects

def sortObjectsByDate(tasks, advices, appointments):

    objects_of_the_day = tasks['day'] + advices['day'] + appointments['day']
    objects_of_the_week = tasks['week'] + advices['week'] + appointments['week']
    objects_of_the_month = tasks['month'] + advices['month'] + appointments['month']

    sorted_objects_day = sortObjects(objects_of_the_day)
    sorted_objects_week = sortObjects(objects_of_the_week)
    sorted_objects_month = sortObjects(objects_of_the_month)

    sorteds_objects = {
        'day': sorted_objects_day,
        'week': sorted_objects_week,
        'month': sorted_objects_month
    }

    return sorteds_objects

def sortObjects(unsorted_obejcts):

    sorted_objects = sorted(
    unsorted_obejcts,
    key=lambda object_TAA: datetime.strptime(getDateByDjangoDate(getFinishDate(object_TAA)), '%d/%m/%y (%H:%M)'), reverse=True
    )

    return sorted_objects

def isTheSameDay(object_TAA, day_string):

    date_finish = getFinishDate(object_TAA)
    date_finish_string = date_finish.strftime("%d/%m/%Y")
    if day_string == date_finish_string:
        return True
    return False

def isTheSameWeek(object_TAA, day_string):
    
    today_week = datetime.strptime(day_string,'%d/%m/%Y')
    today_week = today_week.isocalendar()[1]
    date_finish = getFinishDate(object_TAA)
    week_finish = date_finish.isocalendar()[1]
    if today_week == week_finish:
        return True
    return False

def isTheSameMonth(object_TAA, day_string):

    today_month = datetime.strptime(day_string,'%d/%m/%Y')
    today_month = today_month.isocalendar()[0]
    date_finish = getFinishDate(object_TAA)
    month_finish = date_finish.isocalendar()[0]
    if today_month == month_finish:
        return True
    return False

def getRowsTAA(objects, numberOfTAARows):

    rows = {} 

    for object_TAA in objects:
        numberOfRow = numberOfTAARows[object_TAA]
        rows[object_TAA] = []
        for i in range(0, numberOfRow):
            rows[object_TAA].append([])
            for j in range(0, 3):
                if(len(objects[object_TAA]) > 0):
                    object_TAA_toPut = getObjectTAAToPut(objects[object_TAA][0])
                    rows[object_TAA][i].append(object_TAA_toPut)
                    objects[object_TAA].pop(0)

    return rows

def getObjectTAAToPut(obejct_TAA):

    pk = obejct_TAA.pk
    type_TAA = obejct_TAA.type_TAA
    content_TAA = getContent(obejct_TAA)
    priority_name, priority_id = getPriorityNameAndId(obejct_TAA)
    finish_date = getDateByDjangoDate(getFinishDate(obejct_TAA))

    return {
        'pk': pk,
        'type': type_TAA,
        'content': content_TAA,
        'priority': priority_name,
        'priority_id': priority_id,
        'finish_date': finish_date
    }



def getPriorityNameAndId(object_TAA):

    priority = getPriority(object_TAA)
    if priority == 1:
        return 'Low', 'low'
    elif priority == 2:
        return 'Medium', 'medium'
    elif priority == 3:
        return 'High', 'high'
    elif priority == 4:
        return 'Very High', 'veryhigh'
    return None, None

def getDayWeekName():

    dia = datetime.today().weekday()

    if dia == 0:
        return 'Monday'
    elif dia == 1:
        return 'Tuesday'
    elif dia == 2:
        return 'Wednesday'
    elif dia == 3:
        return 'Thursday'
    elif dia == 4:
        return 'Friday'
    elif dia == 5:
        return 'Saturday'
    elif dia == 6:
        return 'Sunday'
    else:
        return 'error'

def getToday():

    today = datetime.now()
    today = today.strftime("%d/%m/%Y")
    return today