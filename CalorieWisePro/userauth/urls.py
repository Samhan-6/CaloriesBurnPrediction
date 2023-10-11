from django.urls import path

import userauth.views

urlpatterns = [
    path('', userauth.views.index, name = 'index'),
    path('home/', userauth.views.home, name = 'home'),
    path('home/signup/', userauth.views.signup, name = 'signup'),
    path('home/signin/', userauth.views.signin, name = 'login'),
    path('home/signout/', userauth.views.signout, name = 'logout'),
    path('profile/<username>', userauth.views.profile, name = 'profile'),

]