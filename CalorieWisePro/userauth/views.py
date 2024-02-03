import logging

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse

from userauth.forms import CustomUserCreationForm
import pickle
import numpy as np

from .forms import PredictionForm


# Create your views here.
def index(request):
    return render(request, '../templates/index.html')


def home(request):
    if request.user.is_authenticated:
        form = PredictionForm()
        return render(request, "home.html", {'form':form})
    else:
        return redirect("/home/signin/")


def getPrediction(X):
    try:
        with open('/Users/samhan_6/Documents/Final Project/SamhanShuhaib st20267818/CaloriesBurnPrediction/CalorieWisePro/machineLearningModel/model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

            input_data = np.asarray(X, dtype=object)
            input_data_reshaped = input_data.reshape(1, -1)
            prediction = model.predict(input_data_reshaped)
            return prediction

    except EOFError:
        logging.error("EOFError occurred while loading the model.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

def prediction(request):
    form = PredictionForm(request.POST)

    if form.is_valid():
        gender = request.POST['Gender']
        if gender == 'Male':
            gender_numeric = 0
        else:
            gender_numeric = 1
        age = request.POST['Age']
        height = request.POST['Height']
        weight = request.POST['Weight']
        duration = request.POST['Duration']
        heart_rate = request.POST['Heart_Rate']
        body_temp = request.POST['Body_Temp']

        X = [gender_numeric, age, height, weight, duration, heart_rate, body_temp]

        prediction = getPrediction(X)

        if prediction is not None:
            return render(request, 'pred_result.html', {'prediction': prediction})
        else:
            return render(request, 'home.html', {'form': form})
    else:
        return render(request, 'home.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect("/home")

    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, "signup.html", {"form": form})

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have signed up successfully")
            login(request, user)
            return redirect("/home")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, "signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect("/home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("/home")

        else:
            form = AuthenticationForm()
            return render(request, "signin.html", {"form": form})

    else:
        form = AuthenticationForm()
        return render(request, "signin.html", {"form": form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    logout(request)
    return redirect("/home")


def profile(request, username):
    user = User.objects.get(username=username)

    context = {
        'user': user,
    }
    return render(request, context)