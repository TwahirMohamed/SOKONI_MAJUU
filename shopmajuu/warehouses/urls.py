from django.urls import path
from . import views
from .views import display

urlpatterns = [
    path('display/', display, name="display"),
]