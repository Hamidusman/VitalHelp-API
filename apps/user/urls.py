from django.urls import path
from . import views
urlpatterns=[
    path('', views.PatientViewSet.as_view())
]