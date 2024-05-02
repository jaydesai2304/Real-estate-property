from django.contrib import admin
from .models import Member, Add, Contact


class Memberadmin(admin.ModelAdmin):
     list_display = ("username", "email","phone_no","password","gender",)

admin.site.register(Member, Memberadmin)


class addpropertyadmin(admin.ModelAdmin):
     list_display = ("status","property","location","bhk","city","name","image",)

admin.site.register(Add,addpropertyadmin)

class contactadmin(admin.ModelAdmin):
     list_display = ("fname","lname","email","message",)

admin.site.register(Contact, contactadmin)




