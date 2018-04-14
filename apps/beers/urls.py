from django.urls import path
from . import views

urlpatterns = [
    # ex: /beers/
    path('', views.index, name='index'),
    # ex: /beers/5/
    path('<int:beer_id>/', views.detail, name='detail'),
]
