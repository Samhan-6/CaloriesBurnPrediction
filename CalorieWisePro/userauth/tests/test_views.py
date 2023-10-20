from django.test import TestCase, Client
from django.urls import reverse
from userauth.views import *

class TestView(TestCase):

    def setUp(self):
        self.client = Client()


    def test_view_index_route(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_view_home_route(self):
        response = self.client.get('/home/signin/')
        self.assertEquals(response.status_code, 200)

    def test_view_signup_route(self):
        response = self.client.get('/home/signup/')
        self.assertEquals(response.status_code, 200)

    def test_view_signin_route(self):
        response = self.client.get('/home/signin/')
        self.assertEquals(response.status_code, 200)