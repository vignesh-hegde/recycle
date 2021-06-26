from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from one import models
from service.models import Profile

class Upload(forms.ModelForm ,forms.Form):
    email_confirm = forms.EmailField()
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5})
    )
    class Meta:
        model = models.Userdata
        fields ='__all__'
    
    def clean(self):
        cd = self.cleaned_data
        try:
            e = cd['email']
        except:
            raise ValidationError("Email_Error")
        try:
            c = cd['email_confirm']
        except:
            raise ValidationError("Email_Confirmation_Error")
        try:
            p = cd['pincode']
        except:
            raise ValidationError("Pincode_Error")
        try:
            ph = cd['phone']
        except:
            raise ValidationError("Phone_Error")
        
        if e != c:
            raise ValidationError("Email_Confirmation_Error")
        
        if ph> 9999999999 or ph< 1000000000:
            print("HELLO 2")
            raise ValidationError("Phone_Error")
        
        if str(p) not in list(map(str,User.objects.all())):
            raise ValidationError("Pincode_Error")
        try:
            ad = cd['address']
            if len(ad)>490:
               raise ValidationError("Address_Error")  
        except:
            raise ValidationError("Address_Error")    
        
        return cd