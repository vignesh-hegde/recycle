from django.db import models
import uuid

# Create your models here.
class Userdata(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    pincode = models.IntegerField()
    address = models.CharField(max_length=500)
    id = models.UUIDField(
     primary_key = True,
     default = uuid.uuid4,
     editable = False)

    def __str__(self):
        return str(self.name)