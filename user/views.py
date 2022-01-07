from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view
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
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        },
        status=status.HTTP_201_CREATED
        )
