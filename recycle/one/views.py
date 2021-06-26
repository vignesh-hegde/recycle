from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from one import forms
import smtplib
from recycle import hello_world
from one.user_email_messages import get_message



def send_mail(name,email):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('recyclesdh@gmail.com',hello_world.something())
    SUBJECT = "Pick Up Request Accepted"
    TEXT =  get_message(name)
    server.sendmail('Team Recycle',email,'Subject: {}\n\n{}'.format(SUBJECT, TEXT))
    server.close()
    
def index(request):
    return render(request,'user/index.html')

def upload(request):
    form = forms.Upload()
    if request.method == 'POST':
        form = forms.Upload(request.POST)
        if form.is_valid():
            form.save(commit=True)
            send_mail(form.cleaned_data["name"],form.cleaned_data["email"])
            return HttpResponseRedirect('/users/home/')

    return render(request,'user/upload.html',{'form':form})

def contact(request):
       return render(request,'user/contact.html')