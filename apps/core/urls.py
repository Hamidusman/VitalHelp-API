from django.urls import path
from . import views
urlpatterns = [
    path('pres', views.PrescriptionView.as_view())
]