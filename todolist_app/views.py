from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context={
        'welcome_text':"hey there Home"
        }
    return render(request,'todolist.html',context)
    
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
    