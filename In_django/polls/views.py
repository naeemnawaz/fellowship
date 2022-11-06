from django.shortcuts import render
from django.http import HttpResponse
from polls.models import nearest , away
import requests
import folium 
import pandas as pd

url = 'https://api.npoint.io/f26432e9e880999eeb1b'



def main_request(url):
	r = requests.get(url)
	return r.json()


"""
lat= []
log= []

# filtering dictionary data and append into lists
for item in data['features']:
	lati = item['properties']['LATITUDE']
	logi = item['properties']['LONGITUDE']
	lat.append(lati)
	log.append(logi)


#finding which elements are very closest to each other 
extra = [] 
duplist = [] 
for i in lat:
    if i not in extra:
        extra.append(i)
    else:
        duplist.append(i) # this method catches the first duplicate entries, and appends them to the list


#intialization of map
mapbj = folium.Map(zoom_start=5,location=[44.73397,-68.79244])
      

#evaluating the records which markers should be red or blue
def evaluate_markers(lat,log):
   for lat, log in zip(lat, log):
      if lat not in duplist:
         #make a data frame with dots to show on the map
         folium.Marker(location=[lat,log],icon=folium.Icon(color="red")).add_to(mapbj)
      else:
         folium.Marker(location=[lat,log],icon=folium.Icon(color="blue")).add_to(mapbj)
   return mapbj
"""
#evaluate_markers(lat,log)

def index(request):
	return render(request,'polls/templates/index.html')
def map(request):
    mapbj = folium.Map(zoom_start=5,location=[44.73397,-68.79244])
    #scripts of markers
    data = main_request(url)
    lat=[]
    log=[]
    # filtering dictionrary data and append into list
    for item in data['features']:
        lati = item['properties']['LATITUDE']
        logi = item['properties']['LONGITUDE']
        lat.append(lati)
        log.append(logi)
    #finding which elements are very closest to each other 
    extra = [] 
    duplist = [] 
    for i in lat:
        if i not in extra:
            extra.append(i)
        else:
            duplist.append(i)
    for lat , log in zip(lat,log):
        if lat not in duplist:
            #red = nearest(lat = lat , log=log)
            #blue.save()
            #make a data frame with dots to show on the map
            folium.Marker(location=[lat,log],icon=folium.Icon(color="red")).add_to(mapbj)
        else:
            #blue = away(lat=lat , log=log)
            #blue.save()
            folium.Marker(location=[lat,log],icon=folium.Icon(color="blue")).add_to(mapbj)

    mapbj = mapbj._repr_html_()
    context= {
       'mapbj': mapbj,

    }
    return render(request,'polls/templates/map.html',context)

"""
def index(request):
    data = main_request(url)
    lat= []
    log= []

	# filtering dictionary data and append into lists
    for item in data['features']:
        lati = item['properties']['LATITUDE']
        logi = item['properties']['LONGITUDE']        
        lat.append(lati)
        log.append(logi)


    #finding which elements are very closest to each other 
    extra = [] 
    duplist = [] 
    for i in lat:
        if i not in extra:
        	extra.append(i)
        else:

            duplist.append(i) # this method catches the first duplicate entries, and appends them to the list


    #intialization of map
    mapbj = folium.Map(zoom_start=5,location=[44.73397,-68.79244])

    for lat,log in zip(lat,log):
    	if lat not in duplist:
    	    folium.Marker(location=[lat,log],icon=folium.Icon(color="red")).add_to(mapbj)
    	else:
    		folium.Marker(location=[lat,log],icon=folium.Icon(color="blue")).add_to(mapbj)
    return HttpResponse(mapbj)"""