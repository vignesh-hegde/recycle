from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms.fields import IntegerField
from django.forms.widgets import PasswordInput
from one import models
from django.contrib.auth.models import User
from service.models import Profile

from django.contrib.auth.forms import PasswordResetForm

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email

class userProf(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    btn = forms.CharField()
    class Meta():
        model = User
        fields = ('username','email','password')

    def clean_username(self):
        try:
            un = self.cleaned_data['username']
        except:
            raise ValidationError("Error ocured")
        
        try:
            un = int(un)
        except:
            raise ValidationError('Invalid Pincode')        
        
        if un<100000 or un>999999:
            raise ValidationError('Invalid Pincode')
        
        return un 


class Ver(forms.Form):
    val = forms.CharField(widget = forms.HiddenInput())
    btn = forms.CharField()
    amount = forms.IntegerField(initial=0)
    def clean( self ):
        amt = self.cleaned_data['amount']
        btn = self.cleaned_data['btn']
        if btn=='Approve':
            if amt<1:
                raise ValidationError('Amount_Error_low')
            if amt>3000:
                raise ValidationError('Amount_Error_High')
        return self.cleaned_data