from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login, logout
# Create your views here.
# Register API
class GetUser(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content,status=status.HTTP_202_ACCEPTED)


class RegisterUser(GenericAPIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        return Response("OK")
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token.key
        },
        status=status.HTTP_201_CREATED
        )


class LoginUser(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def get(self, request):
        return Response("ok")
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        
        return Response("Login", status=status.HTTP_202_ACCEPTED)
        
        #return super(LoginUser, self).post(request, format=None)

class LogoutUser(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        logout(request)
        return Response("Logouted", status=status.HTTP_202_ACCEPTED)