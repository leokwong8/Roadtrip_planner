import folium
import openrouteservice
import geopandas as gpd
import pandas as pd
import webbrowser
from geopy.geocoders import Nominatim
from shapely.geometry import Point, LineString
from shapely.ops import nearest_points


def create_html_map(start_input, dest_input):
    # Define the starting point, destination point, and attractions
    geolocator = Nominatim(user_agent="myGeocoder")
    starting_point = geolocator.geocode(start_input)
    destination_point = geolocator.geocode(dest_input)

    tourist_attractions_gdf = gpd.read_file('Tourist_Attractions.geojson')
    national_parks = gpd.read_file('National_Parks.geojson')
    attractions_gdf = pd.concat([tourist_attractions_gdf, national_parks])

    # Replace 'your_api_key' with your actual OpenRouteService API key
    client = openrouteservice.Client(key='5b3ce3597851110001cf624855194dc0c63a4c6c9d6db25d7fcb45b6')

    # Define the route coordinates
    coordinates = [
        (starting_point.longitude, starting_point.latitude),
        (destination_point.longitude, destination_point.latitude)
    ]

    # Get the route from the OpenRouteService API
    route = client.directions(
        coordinates=coordinates,
        profile='driving-car',
        format='geojson'
    )

    # Visualize the route using Folium
    map_route = folium.Map(location=[(starting_point.latitude + destination_point.latitude) / 2, (starting_point.longitude + destination_point.longitude) / 2], zoom_start=5)

    folium.GeoJson(
        route,
        name='Route',
        style_function=lambda x: {'color': 'blue', 'weight': 5}
    ).add_to(map_route)

    # Define the distance threshold
    distance_threshold = 1

    # Create a LineString from the route
    route_line = LineString(route['features'][0]['geometry']['coordinates'])

    # Create a buffer zone around the route
    route_buffer = route_line.buffer(distance_threshold)

    # Filter attractions that fall within the buffer zone
    attractions_gdf["in_buffer"] = attractions_gdf.apply(lambda row: route_buffer.contains(row["geometry"]), axis=1)
    filtered_attractions = attractions_gdf[attractions_gdf["in_buffer"]]

    # Add filtered attractions as small green trees
    for index, row in filtered_attractions.iterrows():
        folium.Marker(
            location=(row.geometry.y, row.geometry.x),
            icon=folium.Icon(color='green', icon='tree', prefix='fa'),
            popup=folium.Popup(row['Name'], max_width=250)
        ).add_to(map_route)
    filename = start_input.split(',')[0]+'_to_ '+dest_input.split(',')[0]+'.html'
    map_route.save('route_map.html')

