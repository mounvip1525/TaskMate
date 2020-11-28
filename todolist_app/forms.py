from django import forms
from todolist_app.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta: #creates an instance of the taskmodel model
        model = TaskModel #the model which we are editing
        fields = ["task","done"] #the fields which we are editing