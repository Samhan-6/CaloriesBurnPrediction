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
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], label='Gender',)
    Age = forms.IntegerField(min_value=0, max_value=100, label='Age')
    Height = forms.FloatField(min_value=0, max_value=300, label='Height (cm)')
    Weight = forms.FloatField(min_value=0, max_value=300, label='Weight (kg)')
    Duration = forms.IntegerField(min_value=0, max_value=120, label='Duration (min)')
    Heart_Rate = forms.IntegerField(min_value=0, max_value=200, label='Heart Rate (bpm)')
    Body_Temp = forms.FloatField(min_value=0, max_value=50, label='Body Temperature (°C)')
