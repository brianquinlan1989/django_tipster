from django.db import models

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
        return "{0} - {1}".format(self.race, self.name)
