from django.contrib import admin
from django.urls import path,include
from todolist_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include('todolist_app.urls')),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
]
