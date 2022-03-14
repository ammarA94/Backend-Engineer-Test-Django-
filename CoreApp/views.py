from django.db.models import Count
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import * 
import secrets,smtplib, ssl,traceback,datetime,sys,os,csv,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
def ShowException(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)    
    print (e)   
def SendEmail(receiver_email):
    try:
        print('receiver_email:',receiver_email)
        AuthentiationCode = secrets.token_hex(7)
        sender_email = "futurex.on.the.go@gmail.com"
        password = "Futurex.on.the.go123"
        subject='You have received your Verification Code.'
        html='<p><strong>Your Verification code is :</strong></p><blockquote><p><span style="font-size:18px"><span style="font-family:Georgia,serif"><strong>'+str(AuthentiationCode)+'</strong></span></span></p></blockquote> '
        message = MIMEMultipart(subject)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email
        # Create the plain-text and HTML version of your message
        body = MIMEText(html, "html")
        message.attach(body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return AuthentiationCode
    except Exception as e:
        ShowException(e)
        return False
            
def SignUp(request):
    try:
        request.session['displayname']
        return HttpResponseRedirect('/index/')
    except:
        template = loader.get_template("Signup.html")
        context = {
            "session":request.session,
        }
        return HttpResponse(template.render(context, request))
@api_view(['POST'])
def RegisterUser(request):
    input_data=request.data    
    username = input_data['username']    
    receiver_email =input_data['email'] 
    password =  input_data['password']
    if User.objects.filter(Email=receiver_email).exists():
        #template = loader.get_template("Signup.html")
        context = {"flag":False,"Msg": 'Email already registered. Please login if this email id belongs to you.' }                    
    else:
        try:
            AuthentiationCode=SendEmail(receiver_email)
            if AuthentiationCode:
                User(UserName=username,Email=receiver_email,Password=password,AuthentiationCode=AuthentiationCode).save()
                template = loader.get_template("AuthenticationVerification.html")
                context = {"flag":True,"AuthType":"Register","email":receiver_email,"Msg": 'Authentication Code successfully sent to your email.'}                    
            else:
                #template = loader.get_template("Signup.html")
                context = { "flag":False,"Msg": 'Email not sent due to problem in email service. Please try again.' }                    
        except Exception as e:
            ShowException(e)  
            #template = loader.get_template("Signup.html")
            context = {"flag":False, "Msg": 'Error in authentication process. Please try again.' }
    return Response(context)      
@api_view(['POST'])
def AuthenticationProcess(request):
    input_data=request.data    
    print("input_data",input_data)
    code = input_data['code']   
    email = input_data['email']
    AuthType = input_data['AuthType']   
    
    if User.objects.filter(AuthentiationCode=code,Email=email).exists():
        if AuthType=='Register':
            #template = loader.get_template("login.html")
            context = { "flag": True,"AuthType":"Register",  "Msg": 'Account created.' }      
        else:
            #template = loader.get_template("updatepassword.html")
            context = { "flag": True,"AuthType":"Forgot", "email":email,"Msg": "Please Enter Your New Password" }                     
    else:   
        template = loader.get_template("AuthenticationVerification.html")            
        context = { "flag": False, "AuthType":AuthType,"Msg": 'Code Not Matched.' ,"email":email}
    return Response(context)      

def Login(request):
    try:
        
        request.session['displayname']
        return HttpResponseRedirect('/index/')

    except:
        template = loader.get_template("login.html")
        context = {
            "session":request.session,
        }
        return HttpResponse(template.render(context, request))       
@api_view(['POST'])
def Authentication(request):
    input_data=request.data
    try:
        email = input_data['email']
        password = input_data['password']
        if User.objects.filter(Email=email,Password=password).exists():
            displayname=User.objects.get(Email=email, Password=password).UserName
            request.session['displayname']=displayname
            return Response({"Flag":True,"Msg":"Logged In"})      
        else:                
            return Response({"Flag":False,"Msg":"Wrong Credentials. Please try again."})      

    except Exception as e:
        ShowException(e)
        return Response({"Flag":False,"Msg":"There seems some problems in performing your operations. Please try again."})      
        
    
@api_view(['GET'])
def Logout(request):
    try:
        del request.session['displayname']
        return Response({"Flag":True,"Msg":"Logged Out"})      
    except:
        return Response({"Flag":True,"Msg":"Logged Out"})      
@api_view(['POST'])
def ForgotPassword(request):
    input_data=request.data        
    forgot_email =input_data['forgot_email']
    template = loader.get_template("login.html")  
    AuthentiationCode=SendEmail(forgot_email)
    if AuthentiationCode:
        if User.objects.filter(Email=forgot_email).exists():
            User.objects.filter(Email=forgot_email).update(AuthentiationCode=AuthentiationCode)
            template = loader.get_template("AuthenticationVerification.html")
            context = { "flag":True,"AuthType":"Forgot","email":forgot_email,"Msg": 'Authentication Code successfully sent to your email.'}                    
        else:
            context = {  "flag":False,"email":forgot_email,"Msg": 'Email is not associated with any account.'}                                
    else:
        context = { "flag":False,"receiver_email":forgot_email, "Msg": 'Email not sent due to problem in email service. Please try again.' }                            
    return Response(context)      
@api_view(['POST'])
def Update_Password(request):
    input_data=request.data    
    email = input_data['emai']
    password = input_data['password'] 
    if User.objects.filter(Email=email).exists():
        User.objects.filter(Email=email).update(Password=password)
        context = { "session": request.session,"Info": 'Password Updated Successfully.'}  
    else:
        context = { "session": request.session,"Info": 'Error Updating your Password.'}    
    template = loader.get_template("login.html")
    return HttpResponse(template.render(context, request))           
        
def Index(request):
    try:
        request.session['displayname']

    except:
        return HttpResponseRedirect('/login/')
    template = loader.get_template("index.html")
    data=[]
    context={}
    print(context)
    return HttpResponse(template.render(context, request))
