from django.urls import path
from . import views
urlpatterns=[
    path('', views.PatientView.as_view())
]