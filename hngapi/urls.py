from django.urls import path
from . import views

urlpatterns = [
    path('hng/', views.stage0),
    path('classify-number', views.classify_number, name='classify-number'),
]
