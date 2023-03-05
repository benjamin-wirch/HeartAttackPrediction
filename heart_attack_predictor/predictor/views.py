from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from os import path
from functools import wraps

TEMPLATE_ROOT = 'predictor'


def control_method(permitted: list):
    def decorator(func):
        @wraps(func)
        def view(request):
            if request.method not in permitted:
                return HttpResponseNotAllowed(permitted)
            return func(request)

        return view

    return decorator


def redirect_to_dashboard(func):
    @wraps(func)
    def view(request):
        if request.user.is_authenticated:
            return redirect('dashboard')

        func(request)

    return view


@control_method(('GET',))
def landing(request):
    return render(request, path.join(TEMPLATE_ROOT, 'landing.html'))


@redirect_to_dashboard
@control_method(('GET', 'POST',))
def signin(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'signin.html'))


@redirect_to_dashboard
@control_method(('GET', 'POST',))
def signup(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'signup.html'))


@control_method(('GET', 'POST',))
def dashboard(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'))


@login_required(login_url='signin')
def stats(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'stats.html'))
