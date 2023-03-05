from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Record
from os import path
from functools import wraps
import json

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

        return func(request)

    return view


@control_method(('GET',))
def landing(request):
    return redirect('signin')


@redirect_to_dashboard
@control_method(('GET', 'POST',))
def signin(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'signin.html'))

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        print(f'{username = }')
        print(f'{password = }')

        acc = authenticate(username=username, password=password)

        if acc:
            login(request, acc)
            return JsonResponse({'success': True})

        return JsonResponse({'success': False})
    except Exception:
        return JsonResponse({'success': False})


@redirect_to_dashboard
@control_method(('GET', 'POST',))
def signup(request):
    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'signup.html'))

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        acc = authenticate(username=username, password=password)

        if acc:
            print(acc)
            login(request, acc)
            return JsonResponse({'success': True})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        Record.objects.create(user=user)

        return JsonResponse({'success': True})
    except Exception:
        import traceback
        print(traceback.format_exc())
        return JsonResponse({'success': False})


@login_required(login_url='signin')
@control_method(('GET', 'POST',))
def create_patient_record(request):
    record = Record.objects.get(pk=request.user.id)

    if not record.is_doctor:
        return redirect('dashboard')

    if request.method == 'GET':
        return render(request, path.join(TEMPLATE_ROOT, 'create_patient_record.html'))

    data = json.loads(request.body)

    print('data = n',)

    username = data.get('username')

    user = User.objects.filter(username=username).first()

    if not user:
        return JsonResponse(
            {
                'success': False,
                'reason': f'No user with {username = }',
            }
        )

    data.pop('username', None)

    record = Record.objects.get(pk=user.id)
    record.name = data.get('name')
    record.age = data.get('age')
    record.sex = data.get('sex')
    record.chest_pain = data.get('chest_pain')
    record.resting_blood_pressure = data.get('resting_blood_pressure')
    record.serum_cholestrol = data.get('serum_cholestrol')
    record.fasting_blood_sugar = data.get('fasting_blood_sugar')
    record.resting_ecg = data.get('resting_ecg')
    record.max_heart_rate = data.get('max_heart_rate')
    record.exercise_induced_angina = data.get('exercise_induced_angina')
    record.fluoroscopy_count = data.get('fluoroscopy_count')
    record.thalassemia = data.get('thalassemia')

    record.save(update_fields=list(data.keys()))

    return JsonResponse({'success': True})


@control_method(('GET', 'POST',))
def dashboard(request):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        record = Record.objects.filter(user=user).first()
        return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'), context={'record': record})
