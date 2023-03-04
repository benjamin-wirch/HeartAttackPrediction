from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from os import path

TEMPLATE_ROOT = 'predictor'


def landing(request):
    return render(request, 'predictor/landing.html')


def signin(request):
    return render(request, path.join(TEMPLATE_ROOT, 'signin.html'))


def signup(request):
    return render(request, path.join(TEMPLATE_ROOT, 'signup.html'))


def dashboard(request):
    return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'))


@login_required
def stats(request):
    return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'))
