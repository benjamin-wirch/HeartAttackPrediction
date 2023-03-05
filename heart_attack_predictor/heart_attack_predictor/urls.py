from django.contrib import admin
from django.urls import path

from predictor.views import landing, dashboard, signin, signup, create_patient_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('create-patient-record/', create_patient_record,
         name='create-patient-record'),
]
