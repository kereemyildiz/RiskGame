from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from game.models import *

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ["id","name","password"]

class SessionSerializer2(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ["id","name","password","admin"]


class AddUserToSessionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField() 
    game_session_id = serializers.IntegerField() 