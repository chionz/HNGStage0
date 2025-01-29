from django.urls import path
from . import views

urlpatterns = [
    path('hng/', views.stage0),
]