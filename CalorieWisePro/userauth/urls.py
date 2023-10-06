from django.urls import path

import userauth.views

urlpatterns = [
    path('home/', userauth.views.home),
    path('home/signup/', userauth.views.signup, name = 'signup'),
    path('home/signin/', userauth.views.signin, name = 'login'),
    path('home/signout/', userauth.views.signout, name = 'logout'),

]