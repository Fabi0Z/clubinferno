from django.shortcuts import render
from .models import Beer


def index(request):
    beers_list = Beer.objects.all()
    context = {'beers_list': beers_list}
    return render(request, 'beers/index.html', context)
