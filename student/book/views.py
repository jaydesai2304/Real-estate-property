from django.shortcuts import render, redirect
from django.template import loader 
from .models import Member, Add, Contact
from django.contrib import messages

def register(request):
     if request.method=="POST":
          fullname = request.POST['fullname']
          username = request.POST['username']
          email = request.POST['email']
          phone_no = request.POST['phone_no']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          gender = request.POST['gender']
     
          if Member.objects.filter(username=username):
               messages.error(request,"Username is already exist!")
               return redirect('register')
          
          if Member.objects.filter(email=email):
               messages.error(request,"Email already registered!")
               return redirect('register')

          if len(phone_no) > 10 or len(phone_no) < 10:
                messages.error(request,"invalid number")
                return redirect('register')
          
          if password != confirm_password:
             messages.error(request,"Password does not match")
             return redirect('register')
          
          if len(password) < 8:
             messages.error(request,"It should be at least 8 characters long") 
             return redirect('register')

          data = Member(fullname=fullname, username=username, email=email, phone_no=phone_no, password=password, confirm_password=confirm_password, gender=gender)
          data.save()
          return redirect('login')
     return render(request, 'register.html')


def login(request):
    if request.method=="POST":
        try:
            user=Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            request.session['email']=user.email
            request.session['username']=user.username
            return render(request,'index.html')
        except:

            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['username']
        return render(request,'login.html')
    except:
        return render(request,'login.html')


def index(request):
     return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')

def agent(request):
     return render(request, 'agent.html')

def list(request):
     return render(request, 'list.html')

def details(request, id):
     data = Add.objects.filter(id=id)
     return render(request, 'details.html', {'data' : data})

def rent(request):
     data = Add.objects.all()
     if data:
          if request.method == "POST":
                    location = request.POST.get('location')
                    rooms = request.POST.get('rooms')

                    data = Add.objects.filter(location=location, bhk=rooms)

                    if not data:
                         messages.error(request," Property Not Found")
                         return redirect('rent')
                    
     return render(request,'rent.html',context={'datas':data})

def sell(request):
     data = Add.objects.all()
     if data:
          if request.method == "POST":
                    location = request.POST.get('location')
                    rooms = request.POST.get('rooms')

                    data = Add.objects.filter(location=location, bhk=rooms)
                    
                    if not data:
                         messages.error(request," Property Not Found")
                         return redirect('sell')
     return render(request,'sell.html',context={'datas':data})

def contact(request):
     if request.method == "POST":
          fname = request.POST['fname']
          lname = request.POST['lname']
          email = request.POST['email']
          message = request.POST['message']

          data = Contact(fname=fname, lname=lname, email=email, message=message)
    
          data.save()
     return render(request, 'contact.html')

def profile(request):
     username = request.session.get('username')
     data = Member.objects.filter(username=username)     
     d = {'username' : data}
     return render(request, 'profile.html', d)

def change(request):
     if request.method=="POST":
          oldpassword = request.POST['old-password']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']

          user = Member.objects.filter(password = oldpassword).first()

          if password != confirm_password:
               messages.error(request,"password does not match")
               return redirect('change')
          
          if user:
               user.password = password
               user.save()
               return redirect('login')
          messages.error(request,"invalid password")
     return render(request, 'change.html')

def add(request):
     if request.method=="POST":
          status = request.POST['status']
          property = request.POST['property']
          location = request.POST['location']
          bhk = request.POST['bhk']
          price = request.POST['price']
          area = request.POST['area']
          bath = request.POST['bath']

          media = request.POST.get('media', None)

          address = request.POST['address']
          city = request.POST['city']
          state = request.POST['state']
          country = request.POST['country']

          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          whatsapp = request.POST['whatsapp']
                
          data = Add(status=status, property=property, location=location, bhk=bhk, price=price, area=area, bath=bath, image=media, address=address, city=city, state=state, country=country, name=name, email=email, phone=phone, whatsapp=whatsapp)
          data.save()
          return redirect('index')
     return render(request, 'add-property.html')

def forgot(request):
     if request.method=="POST":
          username = request.POST['username']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          user = Member.objects.filter(username = username).first()

          if len(password) < 8:
             messages.error(request,"It should be at least 8 characters long") 
             return redirect('forgot')

          if password != confirm_password:
               messages.error(request,"password does not match")
               return redirect('forgot')
          if user:
               user.password = password
               user.save()
               return redirect('login')
          messages.error(request,"invalid username")
     return render(request, 'forgot.html')


