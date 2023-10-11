from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


from userauth.forms import CustomUserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html", {})
    else:
        return redirect("/home/signin/")


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

