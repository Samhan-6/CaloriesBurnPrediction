from django.urls import path

import contact.views

urlpatterns = [
    path('contact/', contact.views.contact_view, name='contact'),
]