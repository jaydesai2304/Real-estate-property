from django.urls import path  
from book import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required 

urlpatterns = [   
    path('', views.index,name="index"),
    path('login/',views.login, name="login"),
    path('register/', views.register, name="register"),   
    path('forgot/', views.forgot, name="forgot"),
    path('logout/',views.logout, name="logout"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('agent/',views.agent, name="agent"),
    path('list/',views.list, name="list"),
    path('details/<id>',views.details, name="details"),
    path('profile/',views.profile, name="profile"),
    path('change/',views.change, name="change"),
    path('add-property/',views.add, name="add-property"),
    path('rent/',views.rent, name="rent"),
    path('sell/',views.sell, name="sell"),
    path('wishlist/',views.wishlist, name="wishlist")
   
] 

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 