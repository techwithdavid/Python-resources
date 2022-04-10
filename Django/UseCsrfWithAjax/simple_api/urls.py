from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('return-message', views.return_message, name='return_message')
]