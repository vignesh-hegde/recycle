from os import name
from django.urls import path
from service import views
from django.contrib.auth import views as auth_views
from service.forms import EmailValidationOnForgotPassword

urlpatterns = [
     path('lists/',views.lists,name="lists"),
     path('register/',views.register,name='register'),
     path('index/',views.index,name='index'),
     path('login/',views.user_login,name="login"),
     path('logout/',views.user_logout,name="logout"),


     path('password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword), name='password_reset'),
     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]



