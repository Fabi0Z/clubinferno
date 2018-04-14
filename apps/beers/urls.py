from django.urls import path
from . import views

urlpatterns = [
    # ex: /beers/
    path('', views.index, name='index'),
]
