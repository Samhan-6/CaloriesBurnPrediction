from django.shortcuts import render

# Create your views here.
def index(request):
    username = "samhan"
    return render(request, "base.html", {"name": username})