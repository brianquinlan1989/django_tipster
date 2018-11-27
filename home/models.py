from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=50, blank=False)
    time = models.CharField(max_length=50, blank=False)
    day = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.name

class Runner(models.Model):
    name = models.CharField(max_length=50, blank=False)
    race = models.ForeignKey(Race, null=False, related_name="runners", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
        
class Selection(models.Model):
    user = models.ForeignKey(User, related_name='selections', null=False, on_delete=models.CASCADE)
    runner = models.ForeignKey(Runner, null=False, related_name="selections", on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} - {1} - {2}".format(self.user, self.runner.race, self.runner.name)
        
class Result(models.Model):
    runner = models.ForeignKey(Runner, null=False, related_name="results", on_delete=models.CASCADE)
    position = models.CharField(max_length=50, blank=False)
    odds = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return "{0} - {1} - {2}".format(self.position, self.runner, self.odds)

    
    
