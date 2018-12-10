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
from home.views import show_home, add_selection, add_selection_confirmed, show_leaderboard, show_your_selection_leaderboard, show_rules
from billing.views import make_payment
# from django.views.static import serve

from accounts.views import signup, show_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    # home urls
    path('', show_home, name="home"),
    path('add_selection/day/<int:day>', add_selection, name="add_selection"),
    path('selection_confirmed/<int:day>', add_selection_confirmed, name="add_selection_confirmed"),
    path('leaderboard/', show_leaderboard, name="leaderboard"),
    path('your_selection/day/<int:day>/user/<int:id>', show_your_selection_leaderboard, name="show_your_selection_leaderboard"),
    path('how to play', show_rules, name='show_rules'),
    # account urls
    path('accounts/profile', show_profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    # billing urls

    path('billing/make_payment/', make_payment, name='make_payment'),
    
    #  path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
