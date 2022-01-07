from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('getuser/', views.GetUser.as_view(), name='GetUser'),
    path('login/', views.LoginUser.as_view(), name='LoginUser'),
    path('logout/', views.LogoutUser.as_view(), name='LogoutUser'),
]