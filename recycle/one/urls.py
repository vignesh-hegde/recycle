from django.urls import path
from one import views

urlpatterns = [
    path('home/',views.index,name="index"),
    path('upload/',views.upload,name="upload"),
    path('contact/',views.contact,name="contact"),
]


