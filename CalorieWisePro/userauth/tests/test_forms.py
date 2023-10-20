from django.contrib.auth.models import User
from django.test import TestCase
from userauth.forms import CustomUserCreationForm, PredictionForm

class TestForms(TestCase):

    # user creation testing
    def test_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'samhan',
            'email': 'samhanse@gmail.com',
            'password1': 'HelloWorld!',
            'password2': 'HelloWorld!'
        })
        self.assertTrue(form.is_valid())

    def test_user_creation_no_data(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_user_creation_form_invalid_password(self):
        # passwords don't match
        form = CustomUserCreationForm(data={
            'username': 'samhan',
            'email': 'samhanse@gmail.com',
            'password1': 'HelloWorld!',
            'password2': 'HelloWorld',
        })
        self.assertFalse(form.is_valid())

    def test_user_creation_form_save(self):
        form = CustomUserCreationForm(data={
            'username': 'samhan',
            'email': 'samhanse@gmail.com',
            'password1': 'HelloWorld!',
            'password2': 'HelloWorld!',
        })
        self.assertTrue(form.is_valid())

        user = form.save()

        saved_user = User.objects.get(username='samhan')
        self.assertEqual(saved_user, user)



    # prediction testing
    def test_prediction_form_valid_data(self):
        form = PredictionForm(data={
            'Gender': 'Male',
            'Age': 25,
            'Height': 175.0,
            'Weight': 70.0,
            'Duration': 60,
            'Heart_Rate': 75,
            'Body_Temp': 37.0,
        })
        self.assertTrue(form.is_valid())
