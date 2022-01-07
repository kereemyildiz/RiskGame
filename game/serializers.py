from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from game.models import *

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ["id","name","password"]