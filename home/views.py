from django.shortcuts import render
from .forms import DayOneSelection
import datetime

# Create your views here.


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def show_home(request):
    start = datetime.time(17, 0, 0)
    end = datetime.time(16, 29, 0)
    race_start_time = time_in_range(start, end, datetime.datetime.now().time())


    user_selection_is_picked_day1 = False
    user_selection_is_picked_day2 = True
    user_selection_is_picked_day3 = True
    user_selection_is_picked_day4 = True
    
    context = {"race_start_time":race_start_time, 'user_selection_is_picked_day1':user_selection_is_picked_day1, 'user_selection_is_picked_day2':user_selection_is_picked_day2, 'user_selection_is_picked_day3':user_selection_is_picked_day3, 'user_selection_is_picked_day4':user_selection_is_picked_day4 }
    
    return render(request, "home/index.html", context )


def show_day1_add_selection(request):
    
    add_selection = DayOneSelection
    return render(request, "home/day1_add_selection.html", {'add_selection':add_selection})