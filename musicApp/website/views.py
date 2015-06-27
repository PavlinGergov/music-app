from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist
from django.views.decorators.csrf import csrf_exempt
import json
import codecs

def index(request):
    return render(request, "index.html")

def get_all_artists(request):
    artist = Artist.objects.all()
    data = []
    artist = [a.__dict__ for a in artist]
    for a in artist:
        data.append({key: a[key] for key in a if key != "_state"})
    return JsonResponse(data, safe=False)

@csrf_exempt
def save_artist(request):
    data = json.loads(request.body.decode('utf-8'))
    data["created"] = data["created"].replace("/", "-")
    print(data);
    new_artist = Artist.objects.create(name=data['name'], created=data['created'], image=data['image'], location=data['additionalInformation']['location'], albums=data['additionalInformation']['albums'], singles=data['additionalInformation']['singles'])
    return JsonResponse(request.POST)

def add_artist(request):
    return render(request, "add-artist.html")

def artist_details(request):
    return render(request, "artist-details.html")

def all_artists(request):
    return render(request, "all-artists.html")
