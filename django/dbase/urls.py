from django.urls import path
from dbase import views

urlpatterns = [
    path('dbase/', views.dbase, name = "dbase"),
]