# Generated by Django 5.0.3 on 2024-04-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('rent', 'Rent'), ('sell', 'Sell')], default='', max_length=10)),
                ('property', models.CharField(choices=[('apartment', 'Apartment'), ('bungalow', 'Bungalow'), ('duplex', 'Duplex'), ('row-house', 'Row-House')], default='', max_length=10)),
                ('bhk', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK'), ('5BHK', '5BHK')], default='', max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('bath', models.CharField(choices=[('1BATH', '1BATH'), ('2BATH', '2BATH'), ('3BATH', '3BATH')], default='', max_length=10)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('whatsapp', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.CharField(max_length=10, verbose_name='Phone number')),
                ('password', models.CharField(default='', max_length=50)),
                ('confirm_password', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='', max_length=10)),
            ],
        ),
    ]
