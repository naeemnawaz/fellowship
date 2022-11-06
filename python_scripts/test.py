import requests
import folium 
import pandas as pd

url = 'https://api.npoint.io/f26432e9e880999eeb1b'



def main_request(url):
	r = requests.get(url)
	return r.json()

data = main_request(url)
lat= []
log= []

"""
#This script is just collect the records BUILDING in API 
for item in data['features']: 
	#print(item['properties']['LATITUDE'])
	if item['properties']['BUILDING'] is not None:
	    num= item['properties']['LATITUDE']
	    num2= item['properties']['LONGITUDE']
	    print('this is working')
	    log.append(num2)
	    lat.append(num)
"""



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

print(dir(mapbj))

#evaluating the records which markers should be red or blue
def evaluate_markers(lat,log):
   for lat, log in zip(lat, log):
      if lat not in duplist:
         #make a data frame with dots to show on the map
         folium.Marker(location=[lat,log],icon=folium.Icon(color="red")).add_to(mapbj)
      else:
         folium.Marker(location=[lat,log],icon=folium.Icon(color="blue")).add_to(mapbj)
   return mapbj

evaluate_markers(lat,log)
"""
for lat ,log in zip(lat, log):
	if lat not in duplist:
		# make a data frame with dots to show on the map..
		folium.Marker(location=[lat,log],icon=folium.Icon(color="red")).add_to(mapbj)
	else:
		folium.Marker(location=[lat,log],icon=folium.Icon(color="blue")).add_to(mapbj)
"""
mapbj.save('out.html')
"""
# evaluate the markers 
near = []
for value in lat:
	if value not in duplist:
		"""


#lat.sort()
#for i in lat:
	#print(i)
	#value = round(i ,)
	#if value == 47:
	#	print(value)
	#	print(i)
"""
df = pd.DataFrame(
	{'LONGITUDE ':log,
	  'LATITUDE ':lat
	})
print(df)
"""

"""

mapbj = folium.Map(zoom_start=5,location=[30.183270,66.996452])
# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':log,
   'lat':lat
   
}, dtype=str)

print('data type is')
print(type(data))

#folium.Marker(location=[ , ],icon= folium.Icon(icon='magnet',prefix='fa',color=
#'red').add_to(mapbj)
#folium.Marker(location=[30.183270,66.996452]).add_to(mapbj)

for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      
   ).add_to(mapbj)
mapbj.save('test.html')
"""