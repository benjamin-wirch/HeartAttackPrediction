from django.contrib import admin
from django.urls import path

from predictor.views import landing, dashboard, signin, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing),
    path('dashboard/', dashboard),
    path('signin/', signin),
    path('signup/', signup),
]
