from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField( max_length=300)
    done=models.BooleanField(default=True)
    
    def __str__(self):
        return self.task + " -" + str(self.done)#to prevent showing 'task1 object' and showing task1 instead
