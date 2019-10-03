# pip install folium
# base examples


# simple example
"""
import folium

# base map
map = folium.Map(location=[35.124567,55.12345], zoom_start = 5)
# save map
map.save("map.html")
"""

# base map
map = folium.Map(location=[35.12345,95.123456], zoom_start = 5, tiles = "Mapbox bright")
#   for black chart use :  tiles= "CartoDB dark_matter"

# adding marker to map
folium.Marker(location=[35.123456,95.012345], popup = "Name for marker", icon=folium.Icon(color = 'gray')).add_to(map)
"""
# adding a few markers
for coordinates in [[35.123456,95.123456],[35.123458,95.123478]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)
"""

# save map
map.save("map.html")

"""

import folium
import pandas as pd


# adding data from a file
data = pd.read_csv("file_name.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

# base map
map = folium.Map(location=[35.123456,95.1234567], zoom_start = 5, tiles = "Mapbox bright")
# for black chart use :  tiles= "CartoDB dark_matter"

#  adding markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation)+" m", icon=folium.Icon(color = 'gray')).add_to(map)

#  save map
map.save("map.html")

"""
"""
#  markers with a diferent colors
import folium
import pandas as pd


data = pd.read_csv("file_name.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


def color_change(height):
    if(height < 1000):
        return('green')
    elif(1000 <= height <3000):
        return('orange')
    else:
        return('red')

# base map
map = folium.Map(location=[57.123456,95.1234567], zoom_start = 5, tiles = "Mapbox bright")
# for black chart use :  tiles= "CartoDB dark_matter"
# adding a markers

for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation), icon=folium.Icon(color = color_change(elevation))).add_to(map)

map.save("map.html")

"""
#  example with another model of markers
import folium
from folium.plugins import MarkerCluster
import pandas as pd


data = pd.read_csv("file_name.txt")
lat = data['LAT']
lon = data['LON']
height = data['ELEV']

#  func to change colors
def color_change(height):
    if(height < 1000):
        return('green')
    elif(1000 <= height <3000):
        return('orange')
    else:
        return('red')

    
map = folium.Map(location=[35.123456,95.1234567], zoom_start = 5, tiles = "Mapbox bright")

# markers
for lat, lon, elevation in zip(lat, lon, height):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(height), color="gray", fill_opacity = 0.9).add_to(map)

# for black chart use :  tiles= "CartoDB dark_matter"
    
map.save("map.html")
"""

"""
# group markers by ...
import folium
from folium.plugins import MarkerCluster
import pandas as pd


data = pd.read_csv("file_name.txt")
lat = data['LAT']
lon = data['LON']
height = data['ELEV']

# change colors
def color_change(height):
    if(height < 1000):
        return('green')
    elif(1000 <= height <3000):
        return('orange')
    else:
        return('red')


map = folium.Map(location=[35.123456, 95.1234567], zoom_start = 5, tiles = "CartoDB dark_matter")

# cluster
marker_cluster = MarkerCluster().add_to(map)

#  for cluster
for lat, lon, elevation in zip(lat, lon, height):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(height), color="gray", fill_opacity = 0.9).add_to(marker_cluster)


map.save("map.html")
"""
