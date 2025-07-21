from django.shortcuts import render
from . models import Project
from contacts.forms import ContactForm

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    form = ContactForm()
    return render(request, 'portfolioapp/homepage.html', {'projects': projects, 'form': form})