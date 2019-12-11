import folium

coords = [29,-99]

def return_map():
    map = folium.Map(location=coords,zoom_start=11)
    return map._repr_html_()
