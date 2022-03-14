from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.Login, name= 'login'),
    path('login/login_authentication/', views.Authentication, name='login_authentication'),
    path('logout/', views.Logout, name= 'logout'),
    
    path('', views.Index , name= ''),
    
    path('Signup/', views.SignUp, name= 'Signup'),    
    path('RegisterUser/', views.RegisterUser, name= 'RegisterUser'), 
    path('AuthenticationProcess/', views.AuthenticationProcess, name= 'AuthenticationProcess'),     
    
    path('forgot_password/', views.ForgotPassword, name='forgot_password'),
    path('UpdatePassword/', views.Update_Password, name='UpdatePassword'),
    path('index/', views.Index, name='index'),
   ]