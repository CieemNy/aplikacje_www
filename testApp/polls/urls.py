from django.urls import path, include
from . import views

urlpatterns = [
    path('osoby/', views.osoba_list),
]