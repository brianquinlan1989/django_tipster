from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
import datetime
from .models import Race, Runner, Selection, Day
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.

#------------------------------------------------------------#

# function to return the time
def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
        
# renders the view for the index/home page
def show_home(request):
    start = datetime.time(23, 0, 0)
    end = datetime.time(22, 59, 0)
    race_start_time = time_in_range(start, end, datetime.datetime.now().time())
    
    winners = 0
    places = 0
    if request.user.is_authenticated:
        for selection in request.user.selections.all():
            if selection.runner.position is 1:
                winners +=1
            elif selection.runner.position is 2 or selection.runner.position is 3 or selection.runner.position is 4:
                 places +=1
                
    return render(request, "home/index.html", {"race_start_time":race_start_time, 'winners':winners, 'places':places})

# renders the view for selecting horses, editing selections. Also if the user is logged in but not paid, this function will be redirected to payment page
def add_selection(request, day):
    # if request.user.profile.paid == False:
    #     return redirect("make_payment")
    
    active_day = get_object_or_404(Day, pk=day)
    if active_day.locked or time_in_range(datetime.time(23, 58, 0), datetime.time(23, 59, 0), datetime.datetime.now().time() ) :
        return redirect("add_selection_confirmed", day)
        
    else:
        races = Race.objects.filter(day = day)
        selections = Selection.objects.filter(user = request.user)
        selected_runners = [selection.runner for selection in selections if selection.runner.race.day_id == day]
 
        return render(request, "home/add_selection.html", {'races':races, 'day':day, 'selected_runners': selected_runners})
            
# renders the view of a user's selections, user can add new slections which will overwrite previous selections(edit)   
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
    
# renders the view of the leaderboard
def show_leaderboard(request):
    profiles = Profile.objects.all()
    runners = Runner.objects.all()
    races = Race.objects.all()
    return render(request, "home/leaderboard.html", {'profiles':profiles, 'runners':runners, 'races':races})
    
# def show_results(request, day):
#     selections = Selection.objects.filter(runner__race__day = day)
#     return render(request, "home/leaderboard.html", {'range':range(1,5), 'selections':selections})

# renders the view when you click on a user's name from the leaderboard    
def show_your_selection_leaderboard(request, day, id):
    profiles = Profile.objects.filter(user=request.user)
    user = get_object_or_404(User, id=id)
    selections = Selection.objects.filter(user=user).filter(runner__race__day = day)
    return render(request, "home/user_selection.html", {'profiles':profiles, 'selections':selections, 'user':user, 'range':range(1,5)})
    
# Rules/How to play
def show_rules(request):
    return render(request, "home/rules.html")
    
# Images
def show_images(request):
    return render(request, "home/images.html")
    
# Course Info
def show_course_info(request):
    return render(request, "home/course_info.html")
