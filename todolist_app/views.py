from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskModel
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    context={
        'welcome_text':"hey there about"
        }
    return render(request,'index.html',context)
def todolist(request):
    if request.method == 'POST':
        form=TaskForm(request.POST or None)
        # print(form)
        if form.is_valid():
            form.save()
        messages.success(request,('New Task Added!'))
        return redirect('todolist')
    else:
        all_tasks=TaskModel.objects.all()
        
        # context={
        #     'welcome_text':"hey there Home"
        #     }
        paginator=Paginator(all_tasks,6)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page) #reloading the data after paginating
        return render(request,'todolist.html',{'all_tasks':all_tasks})
    
def delete_task(request,task_id):
    task=TaskModel.objects.get(pk=task_id)  
    task.delete()
    return redirect('todolist')

def edit_task(request,task_id):
    if request.method == 'POST':
        task_obj=TaskModel.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Edited!'))
        return redirect('todolist')
    else:
        task_obj=TaskModel.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

def completed_task(request,task_id):
    task=TaskModel.objects.get(pk=task_id)  
    task.done=True
    task.save()
    return redirect('todolist')


def pending_task(request,task_id):
    task=TaskModel.objects.get(pk=task_id)  
    task.done=False
    task.save()
    return redirect('todolist')
    
def about(request):
    context={
        'about_text':"hey there about"
        }
    return render(request,'about.html',context)

def contact(request):
    context={
        'contact_text':'hey there contact'
    }
    return render(request,'contact.html',context)
    