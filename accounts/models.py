from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    @property
    def score(self):
        selections = self.user.selections.all()
        return sum([selection.runner.score for selection in selections]) 
    
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)