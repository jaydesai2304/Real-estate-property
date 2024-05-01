from django.contrib import admin  
from django.urls import path, include
from book import views  

urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('', include('book.urls')),
]  
