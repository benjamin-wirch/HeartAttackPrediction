from django.contrib import admin
from django.urls import path

from predictor.views import landing, dashboard, signin, signup, stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('stats/', stats, name='stats'),
]
