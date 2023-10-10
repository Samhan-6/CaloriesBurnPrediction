from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {"form": form}
    return render(request, 'contact.html', context)