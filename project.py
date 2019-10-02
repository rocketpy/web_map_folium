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

#  adding markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation)+" m", icon=folium.Icon(color = 'gray')).add_to(map)

#  save map
map.save("map.html")

"""
