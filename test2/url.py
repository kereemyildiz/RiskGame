from . import views
from django.urls import path

urlpatterns = [
    path('getuser/', views.GetUser.as_view(), name='GetUser'),
]