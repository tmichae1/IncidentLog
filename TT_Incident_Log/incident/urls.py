from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.incident_form, name='report')
]
