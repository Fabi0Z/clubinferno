from django.shortcuts import render
from .models import Sponsor


def index(request):
    sponsors_list = Sponsor.objects.all()
    context = {'sponsors_list': sponsors_list}
    return render(request, 'sponsors/index.html', context)
