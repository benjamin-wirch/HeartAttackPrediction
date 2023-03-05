from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Record
from os import path
from functools import wraps
import json

from tensorflow.keras.models import load_model
import numpy as np


TEMPLATE_ROOT = 'predictor'


def get_model():
    model = load_model('outputdata.h5')
    return model


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

    print(f'{data = }')

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

    record = Record.objects.filter(user=user).first()
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

    model = get_model()
    user_data = np.array([
        record.age,
        record.sex,
        record.chest_pain,
        record.resting_blood_pressure,
        record.serum_cholestrol,
        record.fasting_blood_sugar,
        record.resting_ecg,
        record.max_heart_rate,
        record.exercise_induced_angina,
        record.fluoroscopy_count,
        record.thalassemia,
    ], dtype=int).reshape(1, -1)

    prediction = model.predict(user_data, verbose=0)
    prediction = int(round(prediction[0][0]))

    record.predicted_risk = prediction

    record.save(update_fields=list(data.keys()) + ['predicted_risk'])

    return JsonResponse({'success': True})


def build_data():
    import numpy as np
    import faker
    arr = np.genfromtxt('data/heart.csv', delimiter=',',
                        dtype=int, skip_header=True)

    faker = faker.Faker()

    file = open('data/username-passwords.txt', 'w')

    for idx, row in enumerate(arr[206:], start=1):
        # print(f'{idx = }', end=' | ')
        profile = faker.simple_profile()
        name = profile.get('name')
        password = faker.password()
        username = ''.join(name.split(' ')).lower()

        # print(f'{name = } | {username = } | {password = }')

        user = User.objects.create_user(username=username, password=password)

        record = Record.objects.create(user=user)

        record.name = name
        record.age = row[0]
        record.sex = row[1]
        record.chest_pain = row[2]
        record.resting_blood_pressure = row[3]
        record.serum_cholestrol = row[4]
        record.fasting_blood_sugar = row[5]
        record.resting_ecg = row[6]
        record.max_heart_rate = row[7]
        record.exercise_induced_angina = row[8]
        record.fluoroscopy_count = row[9]
        record.thalassemia = row[10]
        record.predicted_risk = row[11]

        record.save(update_fields=[
            'name',
            'age',
            'sex',
            'chest_pain',
            'resting_blood_pressure',
            'serum_cholestrol',
            'fasting_blood_sugar',
            'resting_ecg',
            'max_heart_rate',
            'exercise_induced_angina',
            'fluoroscopy_count',
            'thalassemia',
            'predicted_risk',
        ])

        file.write(f'{username = } | {password = } | {name = }')

    file.close()


@control_method(('GET',))
def dashboard(request):
    # build_data()
    user = User.objects.filter(username=request.user.username).first()
    record = Record.objects.filter(user=user).first()
    if record.is_doctor:
        patients = Record.objects.filter(
            predicted_risk=True)[:9][::-1]
        return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'), context={'patients': patients, 'record': record})
    return render(request, path.join(TEMPLATE_ROOT, 'dashboard.html'), context={'record': record})
