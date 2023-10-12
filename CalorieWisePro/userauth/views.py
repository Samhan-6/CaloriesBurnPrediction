from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
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
    return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        form = PredictionForm()
        return render(request, "home.html", {'form':form})
    else:
        return redirect("/home/signin/")



def getPrediction(X):
    model = pickle.load(open('model.pkl', 'rb'))
    prediction = model.predict(X.reshape(1, -1))

    return prediction[0]


def predict(request):
    X = np.array([
        request.POST['Gender'],
        request.POST['Age'],
        request.POST['Height'],
        request.POST['Weight'],
        request.POST['Duration'],
        request.POST['Heart_Rate'],
        request.POST['Body_Temp'],
    ])

    prediction = getPrediction(X)

    context = {
        'prediction': prediction,
    }
    return render(request, 'pred_result.html', context)








'''

def predict(request):
    gender = request.POST['Gender']
    age = request.POST['Age']
    height = request.POST['Height']
    weight = request.POST['Weight']
    duration = request.POST['Duration']
    heart_rate = request.POST['Heart_Rate']
    body_temp = request.POST['Body_Temp']

    X = [gender, age, height, weight, duration, heart_rate, body_temp]

    result = getPrediction(X)

    return render(request, 'pred_result.html', {'result': result})

'''


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


def signout(request):
    logout(request)
    return redirect("/home")


def profile(request, username):
    user = User.objects.get(username=username)

    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)