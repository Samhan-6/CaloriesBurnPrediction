from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PredictionForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], label='Gender')
    age = forms.IntegerField(min_value=0, max_value=100, label='Age')
    height = forms.FloatField(min_value=0, max_value=300, label='Height (cm)')
    weight = forms.FloatField(min_value=0, max_value=300, label='Weight (kg)')
    duration = forms.IntegerField(min_value=0, max_value=120, label='Duration (min)')
    heart_rate = forms.IntegerField(min_value=0, max_value=200, label='Heart Rate (bpm)')
    body_temp = forms.FloatField(min_value=0, max_value=50, label='Body Temperature (°C)')
