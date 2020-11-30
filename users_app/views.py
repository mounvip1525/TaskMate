from django.shortcuts import render,redirect
from .forms import CustomRegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        register_form=CustomRegistrationForm(request.POST) #request.POST has all the content entered by the user
        if register_form.is_valid():
            register_form.save() #saving to db
            messages.success(request,('New User Created,Login now!'))
            return redirect('register')
    else:
        register_form=CustomRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})