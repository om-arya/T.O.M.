from django.shortcuts import render
from django.http import HttpResponse
from djangofiles.schedule import generate_schedule

def home_view(request):
    return render(request, 'home.html')

def tom_view(request):
    return render(request, 'tom.html')

def about_us_view(request):
    return render(request, 'about-us.html')

def our_mission_view(request):
    return render(request, 'our-mission.html')

def schedule_view(request):
    return render(request, 'schedule.html')

def submit_form(request):
    if request.method == 'GET':
        EVENTS = request.GET.get('events')
        ADDITIONAL_NOTES = request.GET.get('additionalNotes')
        result = generate_schedule(EVENTS, ADDITIONAL_NOTES)
        return render(request, 'schedule.html', {'result': result.text})
    else:
        return HttpResponse("Only GET method is allowed.")