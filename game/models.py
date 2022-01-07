from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.deletion import CASCADE
# Create your models here.

# Game Session Object
class GameSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=True)
    admin = models.ForeignKey(User, on_delete=CASCADE)
    # One to Many relasnsip
    #users = models.



class Player(models.Model):
    # Player is connected with userID
    
    # If user only be deleted if associated player deleted
    # One to One
    userId = models.OneToOneField(User, on_delete=models.PROTECT)

    # If session is deleted, this player will be also deleted
    # One to Many
    session_at = models.ForeignKey(GameSession,on_delete=models.CASCADE)


    def addPlayer(self, user : User):
        userID = user.pk