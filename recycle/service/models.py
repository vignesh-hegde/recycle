from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    User._meta.get_field('email')._unique = True
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        
        )

    user_phone =  models.IntegerField()
   #on_delete=models.DO_NOTHING,

    def __str__(self):
        return self.user.username