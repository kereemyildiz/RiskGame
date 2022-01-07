from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status

from game.serializers import *


# Create your views here.


class CreateSession(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = SessionSerializer
    def get(self, request):
        return Response("Create Session", status=status.HTTP_200_OK)
    def post(self, request):

        #GameSession.objects.create(name, password, admin)
        print(request.data)
        tempReq = request.data.copy()
        print(tempReq)
        tempReq["admin"]=request.user.pk
        print(tempReq)
        serializer = SessionSerializer2(data=tempReq)
        
        serializer.is_valid(raise_exception=True)
       
        
        
        session = serializer.save()
        
        Player.objects.create(userId = request.user, session_at= session)
        return Response({
        "SessionName": tempReq["name"],
        "SessionPassword" : tempReq["password"],
        "OwnerName": User.objects.get(pk=tempReq["admin"]).username
        }, status=status.HTTP_201_CREATED)





# Devam edecek şablon
class AddUserToSession(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AddUserToSessionSerializer
    def get(self,request):
        return Response("Create Session", status=status.HTTP_200_OK)
    def post(self,request):
        pass
        # Create Player from User
        result = AddUserToSessionSerializer(request.data)
        print(result["user_id"].value)
        # Make Player to being added to the session
        Player.objects.create(userId = User.objects.get(pk=result["user_id"].value), session_at = GameSession.objects.get(pk=result["game_session_id"].value))
        return Response("The user:" + str(User.objects.get(pk=result["user_id"].value).username) + " is added to session", status=status.HTTP_202_ACCEPTED)