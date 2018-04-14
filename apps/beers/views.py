from django.http import HttpResponse
from .models import Beer


def detail(request, beer_id):
    return HttpResponse("You're looking at beer %s." % beer_id)


def index(request):
    last_beer = Beer.objects.all()
    output = ', '.join([b.name for b in last_beer])
    return HttpResponse(output)
