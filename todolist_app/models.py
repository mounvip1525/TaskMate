from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task=models.CharField( max_length=300)
    done=models.BooleanField(default=True)
    
    def __str__(self):
        return self.task + " -" + str(self.done)#to prevent showing 'task1 object' and showing task1 instead
