from django.contrib import admin
from .models import Race, Runner, Selection, Day

# Register your models here.
admin.site.register(Race)
admin.site.register(Runner)
admin.site.register(Selection)
admin.site.register(Day)
