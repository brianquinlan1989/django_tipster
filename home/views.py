from django.shortcuts import render, get_object_or_404, HttpResponse
import datetime
from .models import Race, Runner, Selection
from accounts.models import Profile
from django.contrib.auth.models import User


# Create your views here.


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def show_home(request):
    start = datetime.time(17, 0, 0)
    end = datetime.time(13, 46, 0)
    race_start_time = time_in_range(start, end, datetime.datetime.now().time())


    user_selection_is_picked_day1 = False
    user_selection_is_picked_day2 = False
    user_selection_is_picked_day3 = False
    user_selection_is_picked_day4 = False
    
    context = {"race_start_time":race_start_time, 'user_selection_is_picked_day1':user_selection_is_picked_day1, 'user_selection_is_picked_day2':user_selection_is_picked_day2, 'user_selection_is_picked_day3':user_selection_is_picked_day3, 'user_selection_is_picked_day4':user_selection_is_picked_day4 }
    
    return render(request, "home/index.html", context )


def add_selection(request, day):
        races = Race.objects.filter(day = day)
        return render(request, "home/add_selection.html", {'races':races, 'day':day})
        
def add_selection_confirmed(request, day):
    
    selections = Selection.objects.filter(user=request.user)
    for selection in selections:
        if selection.runner.race.day == day:
            selection.delete()
    
    for key,value in request.POST.items():
        if key != 'csrfmiddlewaretoken' and key != 'day':
            r = Runner.objects.filter(name = value)[0]
            selection = Selection(runner = r,  user = request.user)
            selection.save()
     
    return render(request, "home/add_selection_confirmed.html")
    

def show_leaderboard(request):
    profiles = Profile.objects.all()

    return render(request, "home/leaderboard.html", {'profiles':profiles})
    
def show_your_selection_leaderboard(request, day, id):
    profiles = Profile.objects.filter(user=request.user)
    user = get_object_or_404(User, id=id)
    selections = Selection.objects.filter(user=user).filter(runner__race__day = day)
    return render(request, "home/user_selection.html", {'profiles':profiles, 'selections':selections, 'user':user, 'range':range(1,5)})


def show_rules(request):
    return render(request, "home/rules.html")