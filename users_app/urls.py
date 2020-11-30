from django.urls import path
from users_app import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register,name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name='login'), #either create a folder with name registration in the templates folder and have a login.html file in it or mention the template name like here
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),   
]