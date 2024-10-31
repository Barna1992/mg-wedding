from django.shortcuts import render, redirect
from .models import Allergy
from datetime import datetime

wedding_date = datetime(2025, 6, 7, 10, 30)



def home(request):
    return render(request, 'evento/home.html', {'wedding_date': wedding_date})

def submit_allergy(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        allergia = request.POST.get('allergia')

        # Create a new Allergy record
        Allergy.objects.create(nome=nome, allergia=allergia)

        # Redirect to the homepage
        return redirect('home')  # Replace 'home' with the actual name of your homepage URL pattern

    # If not POST, just redirect to the homepage
    return redirect('home')


def allergie_view(request):
    allergies = Allergy.objects.all()
    return render(request, 'evento/allergies_list.html', {'allergies': allergies})