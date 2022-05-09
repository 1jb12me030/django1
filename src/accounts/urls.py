from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', home ,name='home'),
    path('register',register_attempt,name='register_attempt'),
    path('login',login_attempt,name='login_attempt'),
    path('success',success,name='success'),
    path('token',token_send,name='token_send'),
    path('verify/<auth_token>',verify,name='verify'),
    path('error', error_page ,name='error')
]