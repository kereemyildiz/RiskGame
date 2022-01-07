from . import views
from django.urls import path

urlpatterns = [
    path('createsession/', views.CreateSession.as_view(), name='CreateSession'),
    path('adduser/', views.AddUserToSession.as_view(), name='CreateSession'),
]