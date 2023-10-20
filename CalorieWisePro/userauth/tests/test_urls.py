from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userauth.views import index, home, signup, signin, signout, profile, prediction
class TestUrls(SimpleTestCase):
    def test_index_urls_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_home_urls_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_signup_urls_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_signin_urls_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, signin)

    def test_signout_urls_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, signout)

    def test_profile_urls_is_resolved(self):
        url = reverse('profile', args=['profile'])
        self.assertEquals(resolve(url).func, profile)

    def test_prediction_urls_is_resolved(self):
        url = reverse('result')
        self.assertEquals(resolve(url).func, prediction)