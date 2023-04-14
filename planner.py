from getPOI import point_of_interest

KEY = 'AIzaSyA1_GpZ_vaKI7PsUB0Mx-cMtL_1BMyUncg'
POI = point_of_interest(KEY)
tourist_attractions_gdf = POI.get_tourist_attractions()
national_parks = POI.get_national_parks()