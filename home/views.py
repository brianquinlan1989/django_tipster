from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
import datetime
from .models import Race, Runner, Selection, Day
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
    end = datetime.time(16, 59, 0)
    race_start_time = time_in_range(start, end, datetime.datetime.now().time())
    
    return render(request, "home/index.html", {"race_start_time":race_start_time})


def add_selection(request, day):
    if request.user.profile.paid == False:
        return redirect("make_payment")
    
    active_day = get_object_or_404(Day, pk=day)
    if active_day.locked or time_in_range(datetime.time(16, 30, 0), datetime.time(23, 59, 0), datetime.datetime.now().time() ) :
        return redirect("add_selection_confirmed", day)
        
    else:
        races = Race.objects.filter(day = day)
        selections = Selection.objects.filter(user = request.user)
        selected_runners = [selection.runner for selection in selections if selection.runner.race.day_id == day]
 
        return render(request, "home/add_selection.html", {'races':races, 'day':day, 'selected_runners': selected_runners})
            
   
def add_selection_confirmed(request, day):

    selections = Selection.objects.filter(user=request.user)
    for selection in selections:
        if selection.runner.race.day_id == day:
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