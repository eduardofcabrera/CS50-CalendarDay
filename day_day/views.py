import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Advice, Appointment, Task, DayWeek, Routine, RoutineContent
from . import get
from django.core import serializers
from datetime import datetime
# Create your views here.

def index(request):

    if request.method == 'POST':
        return createObject(request)

    if request.user.is_anonymous:    
        return render(request, 'calendarDay/mid-log-out.html')


    rowsTAA = get.getRows(request)
    today = get.getToday()
    weekday = get.getDayWeekName()

    return render(request, 'calendarDay/layout.html', {
        'rows': rowsTAA,
        'today': today,
        'weekday': weekday
    })


def logIn_view(request):

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "calendarDay/mid-log-out.html", {
            "message": "Invalid username and/or password."
    })

def logOut_view(request):
    logout(request)
    print(request.user)
    return HttpResponseRedirect(reverse("index"))

def register(request):

    if request.method == "GET":
        return HttpResponseRedirect(reverse("index"))

    first = request.POST["first"]
    last = request.POST["last"]
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    again = request.POST["again"]

    checkUserRegister(request, first, last, username, email, password, again)

    if password != again:
        return render(request, "calendarDay/mid-log-out.html", {
            "message": "Passwords must match."
        })
    
    try:
        user = User.objects.create_user(first_name=first, last_name=last, username=username, email=email, password=password)
        user.save()
    except IntegrityError:
        return render(request, "calendarDay/mid-log-out.html", {
            "message": "Username already taken."
        })
    

    login(request, user)
    routine = Routine.objects.create()
    user = get.getUserByRequest(request)
    user.user_routine = routine
    user.save()
    return HttpResponseRedirect(reverse("index"))

def checkUserRegister(request, first, last, username, email, password, again):

    if first == '' or last == '' or username == '' or email == '' or password == '' or again == '':
        return render(request, "calendarDay/mid-log-out.html", {
            "message": "All fields must bee filled."
        })
    return None

def TAA_API(request, type_TAA, TAA_id):
    
    TAA_Json = getTAAJson(type_TAA, TAA_id)
    if not TAA_Json:
        return HttpResponse("Error: TAA does not exist")

    return JsonResponse(TAA_Json, status=201)

def getTAAJson(type_TAA, TAA_id):

    TAA = check_TAA_type(type_TAA, TAA_id)
    
    if not TAA:
        return None

    routine_content = TAA.routine_content

    days_week = get.getDayWeek(TAA)
    date_created = getDateCreated(routine_content, timezone=0)
    date_finish = getDateFinish(routine_content, timezone=0)

    return {
        "type": type_TAA,
        "TAA_id": TAA.pk,
        "routine_content_id": routine_content.pk,
        "content": routine_content.content,
        "priority": routine_content.priority,
        "date_created": date_created,
        "date_finish": date_finish,
        "day_week": [day.day for day in days_week],
        "is_routine": routine_content.is_routine,
        "active": routine_content.active
    }

def check_TAA_type(type_TAA, TAA_id):
    
    TAA = None
    TAA_special = None
    if type_TAA == 'Task':
        try:
            TAA = get.getTaskByPK(TAA_id)
        except:
            return None
    elif type_TAA == 'Advice':
        try:
            TAA = get.getAdviceByPK(TAA_id)
        except:
            return None
    elif type_TAA == 'Appointment':
        try:
            TAA = get.getAppointmentByPK(TAA_id)
        except:
            return None
    return TAA

def createObject(request):

    data = getData(request)
    if not data:
        return HttpResponseRedirect(reverse("index"))
    routine_content = createRoutineContent(data)
    putTheDayInRoutineContent(routine_content, data)
    object_TAA = createObjectTAA(data['type'], routine_content)
    addObjectToRoutine(request, object_TAA, data)

    return HttpResponseRedirect(reverse("index"))

def createRoutineContent(data):

    routine_content = RoutineContent.objects.create(
        content=data['content'], priority=data['priority'], 
         date_finish=data['date-time'], is_routine=data['is-routine']
        )

    return routine_content

def putTheDayInRoutineContent(routine_content, data):

    days = data['days_of_week']

    if days['monday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=9))
    if days['tuesday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=10))
    if days['wednesday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=11))
    if days['thursday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=12))
    if days['friday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=13))
    if days['saturday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=14))
    if days['sunday'] != None:
        routine_content.day_week.add(DayWeek.objects.get(pk=15))

def createObjectTAA(type, routine_content):
    if type == 'Task':
        task = Task.objects.create(routine_content=routine_content)
        return task
    elif type == 'Appointment':
        appointment = Appointment.objects.create(routine_content=routine_content)
        return appointment
    elif type == 'Advice':
        advice = Advice.objects.create(routine_content=routine_content)
        return advice
    else: return None

def addObjectToRoutine(request, object_TAA, data):

    user = get.getUserByRequest(request)
    user_routine = get.getUserRoutine(user)
    type_TAA = data['type']
    addTypeRoutine(user_routine, object_TAA, type_TAA)

def addTypeRoutine(user_routine, object_TAA, type_TAA):

    if type_TAA == 'Task':
        user_routine.routine_tasks.add(object_TAA)
    elif type_TAA == 'Advice':
        user_routine.routine_advices.add(object_TAA)
    elif type_TAA == 'Appointment':
        user_routine.routine_appointments.add(object_TAA)
    else: return None

def getData(request):


    data = {
        'type': getFormType(request),
        'priority': getFormPriority(request),
        'days_of_week': getFormDaysWeek(request),
        'is-routine': getFormIsRoutine(request),
        'date-time': getFormDateTime(request),
        'content': getFormContent(request)   
    }

    if not data['date-time'] or not data['content']:
        return None

    return data

def getFormType(request):
    return request.POST.get('select-type')

def getFormPriority(request):
    priority = request.POST.get('select-priority')

    if priority == 'Low':
        return 1
    elif priority == 'Medium':
        return 2
    elif priority == 'High':
        return 3
    elif priority == 'Very High':
        return 4
    else: return None

def getFormDateTime(request):

    date = request.POST.get('date')
    time = request.POST.get('time')
    if not date or not time:
        return None
    date_time = date + time
    date_time_obj = datetime.strptime(date_time, '%Y-%m-%d%H:%M')
    return date_time_obj

def getFormDaysWeek(request):

    days_week = {
        'monday': request.POST.get('monday'),
        'tuesday': request.POST.get('tuesday'),
        'wednesday': request.POST.get('wednesday'),
        'thursday': request.POST.get('thursday'),
        'friday': request.POST.get('friday'),
        'saturday': request.POST.get('saturday'),
        'sunday': request.POST.get('sunday')
    } 

    return days_week

def getFormIsRoutine(request):

    is_routine = request.POST.get('is-routine')

    if not is_routine:
        return False
    return True

def getFormContent(request):
    content = request.POST.get('content')
    if not content:
        return None
    return content

def getDateCreated(routine_content, timezone=0):
    return get.getDateByDjangoDate(routine_content.date_created)

def getDateFinish(routine_content, timezone=0):
    return get.getDateByDjangoDate(routine_content.date_finish)

@csrf_exempt
def activeUnactive(request, type_TAA, TAA_id):
    
    if request.method == 'PUT':
        
        user = request.user
        data = json.loads(request.body)
        
        TAA = check_TAA_type(type_TAA, TAA_id)
        if TAA == None:
            return None

        routine_content = get.getRoutineContent(TAA)

        if data['active']:
            activeTAA(routine_content)
        else:
            unactiveTAA(routine_content)
    
    return None

def activeTAA(routine_content):

    routine_content.active = True
    routine_content.save()


def unactiveTAA(routine_content):

    routine_content.active = False
    routine_content.save()

@csrf_exempt
def editTAA(request, type_TAA, TAA_id):
    
    if request.method == 'PUT':
        
        user = request.user
        data = json.loads(request.body)
        
        TAA = check_TAA_type(type_TAA, TAA_id)
        if TAA == None:
            return None

        routine_content = get.getRoutineContent(TAA)
        routine_content.content = data['text']
        routine_content.save()
    
    return None

@csrf_exempt
def deleteTAA(request, type_TAA, TAA_id):
    
    if request.method == 'PUT':
        
        TAA = check_TAA_type(type_TAA, TAA_id)
        if TAA == None:
            return None

        TAA.delete()
    
    return None


    
    
    
    
