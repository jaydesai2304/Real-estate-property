# Generated by Django 5.0.4 on 2024-04-26 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lname',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add')),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.member')),
            ],
        ),
    ]