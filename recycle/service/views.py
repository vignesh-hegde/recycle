from recycle.hello_world import something
from django import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from service import forms
from django.urls import reverse
from recycle import hello_world
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from service import user_email_messages

from one.models import Userdata
from random import randint 
import smtplib
from service.forms import userProf


def index(request):
    return render(request,'service/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form  = userProf(data=request.POST)
        if user_form.is_valid() :
            if 'OTP' in request.POST:
                print("HELLO WORLD")
            else:
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                registered = True
    else:
        user_form = userProf()
    print(user_form.errors)
    if str(user_form.errors)=='<ul class="errorlist"><li>email<ul class="errorlist"><li>User with this Email address already exists.</li></ul></li></ul>':
        messages.error(request,"Email Already in Use")
    if str(user_form.errors)=='<ul class="errorlist"><li>username<ul class="errorlist"><li>Invalid Pincode</li></ul></li></ul>':
        messages.error(request,"Invalid Pincode")
    if str(user_form.errors)=='<ul class="errorlist"><li>username<ul class="errorlist"><li>A user with that username already exists.</li></ul></li></ul>':
        messages.error(request,"We have our Agent at this location. ")
        messages.error(request,"Have any issue? please email us at recyclesdh@gmail.com")
    return render(request,'service/registration.html',
        {"user_from":user_form,"registered":registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('service:index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('service:index'))

            else:
                messages.error(request, "Please Login Again")
                return render(request,"service/login.html",{})
        else:
            messages.error(request, "Invalid Credentials")
            return render(request,"service/login.html",{})
    else:
        return render(request,"service/login.html",{})


def genCoup():
    return randint(1000_0000_000_0000,9999_9999_9999_9999)

def deldata(uid):
    Userdata.objects.get(id = uid).delete()
    

def send_mail(name,email,amount,confirm,uid):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('recyclesdh@gmail.com',hello_world.something())
    deldata(uid)
    if confirm:
        SUBJECT = "Pick Up Approved"
        c = genCoup()
        TEXT = user_email_messages.get_approved_message(name,c,amount)
    else:
        SUBJECT = "Pick Up Rejected"
        TEXT = user_email_messages.get_rejected_message(name)
    server.sendmail('Team Recycle',email,'Subject: {}\n\n{}'.format(SUBJECT, TEXT))
    server.close()

@login_required
def lists(request):
    form = forms.Ver()
    all_objects = Userdata.objects.filter(pincode = request.user.username)
    if request.method == 'POST':
        form = forms.Ver(request.POST)
        if form.is_valid():
            cond = form.cleaned_data['btn']
            uid = form.cleaned_data['val']
            amount = form.cleaned_data['amount']
            #inst = Userdata.objects.get(id=uid)
            name = Userdata.objects.filter(id=uid).values('name')[0]["name"]
            email = Userdata.objects.filter(id=uid).values('email')[0]["email"]
            if cond.lower() == 'approve':
                send_mail(name,email,amount,confirm=True,uid = uid)
                return HttpResponseRedirect('/service/lists/')
            elif cond.lower() == 'reject':
                send_mail(name,email,amount,confirm=False,uid = uid)
                return HttpResponseRedirect('/service/lists/')

    return render(request, 'service/verify.html', {'all_objects': all_objects,'form':form})