from django.shortcuts import render
import os

TEMPLATE_ROOT = 'predictor'


def home(request):
    return render(request, os.path.join(TEMPLATE_ROOT, 'home.html'))


def signin(request):
    return render(request, os.path.join(TEMPLATE_ROOT, 'signin.html'))


def signup(request):
    return render(request, os.path.join(TEMPLATE_ROOT, 'signup.html'))


def dashboard(request):
    return render(request, os.path.join(TEMPLATE_ROOT, 'dashboard.html'))
