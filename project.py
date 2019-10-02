# pip install folium

import folium

# base map
map = folium.Map(location=[35.124567,55.12345], zoom_start = 5)

# save map
map.save("map.html")


