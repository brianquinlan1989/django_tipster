"""django_tipster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import show_home, add_selection, add_selection_confirmed, show_leaderboard, show_your_selection

from accounts.views import signup, show_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home, name="home"),
    path('add_selection/day/<int:day>', add_selection, name="add_selection"),
    # path('edit_selection/day/<int:id>', edit_selection, name="edit_selection"),
    path('selection_confirmed/', add_selection_confirmed, name="add_selection_confirmed"),
    path('leaderboard/', show_leaderboard, name="leaderboard"),
    path('your_selection/day', show_your_selection, name="show_your_selection"),
    
    path('accounts/profile', show_profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
]
