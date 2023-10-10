from django.urls import path

import about.views

urlpatterns = [
    path('about/', about.views.about_us, name = 'about'),
]