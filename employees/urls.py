from django.urls import path
from . import views

app_name = "employees"
urlpatterns = [
     path('login_user', views.login_user, name='login'),
     path('register', views.registerUser, name='register'),
     path('logout_user', views.logout_user, name='logout'),
 ]

