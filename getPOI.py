import googlemaps
import geopandas as gpd
from shapely.geometry import Point
class point_of_interest:
    def __init__(self, key):

        self.gmaps = googlemaps.Client(key=key)
        self.us_states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
                    'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
                    'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
                    'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
                    'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
                    'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
                    'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
                    'Tennessee','Texas','Utah','Vermont','Virginia','Washington',
                    'West Virginia','Wisconsin','Wyoming']
        self.columns = ['Name', 'State', 'Type']

    def get_tourist_attractions(self):
        output_gdf = gpd.GeoDataFrame(columns=self.columns)
        for state in self.us_states:
            query = f'{state} tourist attractions'
            result = self.gmaps.places(query=query,type='tourist_attraction')
            for place in result['results']:
                name = place['name']
                lat = place['geometry']['location']['lat']
                lng = place['geometry']['location']['lng']
                point =  Point(lng,lat)
                output_gdf = output_gdf.append({'Name':name, 'State':state, 'Type':'TA', 'geometry':point},ignore_index=True)
        output_gdf.crs = 'EPSG:4326'  
        output_gdf.to_file('Tourist_Attractions.geojson', driver='GeoJSON')
        return output_gdf
        pass
    
    def get_national_parks(self):
        output_gdf = gpd.GeoDataFrame(columns=self.columns)
        for state in self.us_states:
            query = f'{state} national park'
            result = self.gmaps.places(query=query,type='park')
            for place in result['results']:
                name = place['name']
                lat = place['geometry']['location']['lat']
                lng = place['geometry']['location']['lng']
                point =  Point(lng,lat)
                output_gdf = output_gdf.append({'Name':name, 'State':state, 'Type':'NP', 'geometry':point},ignore_index=True)
        output_gdf.crs = 'EPSG:4326'  
        output_gdf.to_file('National_Parks.geojson', driver='GeoJSON')
        return output_gdf
        pass
