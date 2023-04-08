import googlemaps
import geopandas as gpd
from shapely.geometry import Point
class point_of_interest:
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyA1_GpZ_vaKI7PsUB0Mx-cMtL_1BMyUncg')
        self.us_states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
                    'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
                    'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
                    'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
                    'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
                    'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
                    'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
                    'Tennessee','Texas','Utah','Vermont','Virginia','Washington',
                    'West Virginia','Wisconsin','Wyoming']
        self.columns = ['name', 'lat', 'lng']
        self.US_POI = gpd.GeoDataFrame(columns=self.columns)
    
    def getDataset(self):

        for state in self.us_states:
            self.query_ta = f'{state} tourist attractions'
            self.query_np = f'{state} national park'
            self.ta_result = self.gmaps.places(query=self.query_ta,type='tourist_attraction')
            self.np_result = self.gmaps.places(query=self.query_np,type='park')
            for ta,np in zip(self.ta_result['results'], self.np_result['results']):
                self.name_ta = ta['name']
                self.name_np = np['name']
                self.lat_ta = ta['geometry']['location']['lat']
                self.lat_np = np['geometry']['location']['lat']
                self.lng_ta = ta['geometry']['location']['lng']
                self.lng_np = np['geometry']['location']['lng']
                self.point_ta =  Point(self.lng_ta,self.lat_ta)
                self.point_np =  Point(self.lng_np,self.lat_np)
                self.US_POI = self.US_POI.append({'name':self.name_ta, 'lat':self.lat_ta, 'lng':self.lng_ta, 'geometry':self.point_ta},ignore_index=True)
                self.US_POI = self.US_POI.append({'name':self.name_np, 'lat':self.lat_np, 'lng':self.lng_np, 'geometry':self.point_np},ignore_index=True)
        return self.US_POI