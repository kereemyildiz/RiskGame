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

       
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = serializer.save()

        Player.objects.create(userId = request.user, session_at= session)
        return Response(SessionSerializer(session).data, status=status.HTTP_201_CREATED)





# Devam edecek şablon
class AddUserToSession(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass
        # Create Player from User

        # Make Player to being added to the session
        return Response("The user" + str(request.user) + " is added to session", status=status.HTTP_202_ACCEPTED)