from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expenses(models.Model):

    title=models.CharField(max_length=100)

    category_options=[
        ('shoping','shoping'),
        ('food','food'),
        ('rent','rent'),
        ('travel','travel'),
        ('fuel','fuel'),
        ('medical','medical'),
        ('education','education'),
        ('investment','investment'),
        ('bills','bills'),
        ('others','others'),


    ]

    category=models.CharField(max_length=20,choices=category_options)
    amount=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)