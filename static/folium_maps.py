import folium
from mongoclient import get_geojson

def return_map(coords):
    inv_coords = [coords[1],coords[0]]
    map = folium.Map(location=inv_coords,zoom_start=5)
    geojson = get_geojson(coords)
    layer = folium.GeoJson(geojson).add_to(map)
    return map
