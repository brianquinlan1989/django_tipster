from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import *

# Create your models here.

class Day(models.Model):
    locked = models.BooleanField()

    def __str__(self):
        return "{0}".format(self.locked)
        
        
class Race(models.Model):
    name = models.CharField(max_length=50, blank=False)
    time = models.CharField(max_length=50, blank=False)
    day = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Runner(models.Model):
    name = models.CharField(max_length=50, blank=False)
    race = models.ForeignKey(Race, null=False, related_name="runners", on_delete=models.PROTECT)
    position = models.IntegerField(default=0)
    odds = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    
    @property
    def score(self):
        multiplier = 1 if self.position == 1 else 0.25
        total_score = round(self.odds * Decimal(multiplier), 2)
        return total_score
        
 
    def __str__(self):
        return "{0} - {1}".format(self.name, self.race)
        
class Selection(models.Model):
    user = models.ForeignKey(User, related_name='selections', null=False, on_delete=models.CASCADE)
    runner = models.ForeignKey(Runner, null=False, related_name="selections", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.user, self.runner.race, self.runner.name, self.created_date)
    

    
    
    
