from django.shortcuts import render
import datetime
from .models import Race, Runner, Selection
from accounts.models import Profile

# Create your views here.


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def show_home(request):
    start = datetime.time(17, 0, 0)
    end = datetime.time(13, 18, 0)
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
        
def add_selection_confirmed(request):
    for key,value in request.POST.items():

        if key != 'csrfmiddlewaretoken' and key != 'day':
            r = Runner.objects.filter(name = value)[0]
            selection = Selection(runner = r,  user = request.user)
            selection.save()
    return render(request, "home/add_selection_confirmed.html", {'selection':selection})

def show_leaderboard(request):
    profiles = Profile.objects.all()
    
    
    return render(request, "home/leaderboard.html", {'profiles':profiles})
    
def show_your_selection(request):
    profiles = Profile.objects.all()
    return render(request, "home/user_selection.html", {'profiles':profiles})
    








#         request.method == "POST"
#         form = RaceSelection(request.POST)
#         selection = form.save(commit=False)
#         selection.user = request.user
#         saved_selection = post.save()
        
#         return render(request, "home/selection_confirmed.html", {'saved_selection':saved_selection})
    
    
# def edit_selection(request):
#     edit_selection = RaceSelection()
#     return render(request, "home/edit_selection.html", {'edit_selection':edit_selection})