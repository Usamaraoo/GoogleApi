from django.shortcuts import HttpResponse, render
import requests
from urllib.parse import urlencode


def map(request):
    if request.method == "POST":
        area = request.POST.get('area')
        print(area)
        lat_long = (extract_lat_lng(area))
        lat = (lat_long[0])
        lng = (lat_long[1])

    context = {'lat': lat, 'lng': lng}
    return render(request, 'map.html', context)


# GeoCoding Api
api_key = 'AIzaSyCI8hoW9BplzJXyxgiiCdZgxnuPHsFezLA'


def extract_lat_lng(address_or_postalcode, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")
