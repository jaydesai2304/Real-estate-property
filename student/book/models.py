from django.db import models

class Member(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=10, verbose_name="Phone number")
    password = models.CharField(max_length=50, default='')
    confirm_password = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=10, choices=GENDER, default='')

class Add(models.Model):
    STATUS = [
        ('rent', 'Rent'),
        ('sell', 'Sell'),
    ]

    PROPERTY = [
        ('apartment', 'Apartment'),
        ('bungalow', 'Bungalow'),
        ('duplex', 'Duplex'),
        ('row-house', 'Row-House'),
    ]

    LOCATION = [
        ('nikol', 'Nikol'),
        ('viratnagar', 'Viratnagar'),
        ('new india-colony', 'New India-colony'),
        ('naroda', 'Naroda'),
        ('bapunagar', 'Bapunagar'),
    ]

    BHK = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
    ]

    BATH = [
        ('1BATH', '1BATH'),
        ('2BATH', '2BATH'),
        ('3BATH', '3BATH'),
    ]

    status = models.CharField(max_length=10, choices=STATUS, default='')
    property = models.CharField(max_length=10, choices=PROPERTY, default='')
    location = models.CharField(max_length=20,choices=LOCATION, default='')
    bhk = models.CharField(max_length=10, choices=BHK, default='')
    price = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    bath = models.CharField(max_length=10, choices=BATH, default='')

    image= models.ImageField(upload_to="media/",default = None)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20 )
    country = models.CharField(max_length=20)

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True)
    phone = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    

class Contact(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=70, blank=True)
    message = models.CharField(max_length=255)
