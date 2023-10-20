from unittest import TestCase

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from contact.models import Contact
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.auth.models import User
from userauth.forms import PredictionForm
from django.urls import reverse
import time
from django.contrib import messages


class TestMySite(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Edge()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def tearDown(self):
        self.browser.quit()

    def test_index_page(self):
        self.browser.get(self.live_server_url + '')
        time.sleep(10)

    def test_signup_button(self):
        self.browser.get(self.live_server_url)

        signup_button = self.browser.find_element(By.LINK_TEXT, "Sign Up For Free")
        self.assertIsNotNone(signup_button)

        signup_button.click()

        self.assertEqual(self.browser.current_url, self.live_server_url + "/home/signup/")
        time.sleep(10)

    def test_login_button(self):
        self.browser.get(self.live_server_url)

        # Wait for the landing content to load
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "landing-content")))

        login_button = self.browser.find_element(By.LINK_TEXT, "Login")
        self.assertIsNotNone(login_button)

        # Click the login button using JavaScript
        self.browser.execute_script("arguments[0].click();", login_button)

        self.assertEqual(self.browser.current_url, self.live_server_url + "/home/signin/")
        time.sleep(10)


    def test_contact_page(self):
        self.browser.get(self.live_server_url)

        # Wait for the landing content to load
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "landing-content")))

        contact = self.browser.find_element(By.LINK_TEXT, "Contact Us")

        contact.click()

        self.assertEquals(self.browser.current_url, self.live_server_url + '/contact/')
        time.sleep(10)


    def test_about_page(self):
        self.browser.get(self.live_server_url)

        # Wait for the landing content to load
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "landing-content")))

        contact = self.browser.find_element(By.LINK_TEXT, "About Us")

        contact.click()

        self.assertEquals(self.browser.current_url, self.live_server_url + '/about/')
        time.sleep(10)


    def test_login(self):
        self.browser.get(self.live_server_url + "/home/signin/")

        username_input = self.browser.find_element(By.ID, "id_username")
        username_input.send_keys("testuser")

        password_input = self.browser.find_element(By.ID, "id_password")
        password_input.send_keys("testpass")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(self.browser, 10).until(EC.url_matches(self.live_server_url + "/home"))

        # Assert that the user is on the homepage
        self.assertEqual(self.browser.current_url, self.live_server_url + '/home/')
        time.sleep(10)


    def test_signup(self):
        self.browser.get(self.live_server_url + "/home/signup/")

        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys("testuser1")

        email_input = self.browser.find_element(By.NAME, "email")
        email_input.send_keys("testuser@example.com")

        password1_input = self.browser.find_element(By.NAME, "password1")
        password1_input.send_keys("testpass123")

        password2_input = self.browser.find_element(By.NAME, "password2")
        password2_input.send_keys("testpass123")

        password2_input.send_keys(Keys.RETURN)

        WebDriverWait(self.browser, 10).until(EC.url_matches(self.live_server_url + '/home/'))

        self.assertEquals(self.browser.current_url, self.live_server_url + '/home/')
        time.sleep(10)














