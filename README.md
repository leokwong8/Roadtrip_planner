# Roadtrip_planner
Road trips are fun, but planning a road trip can be a daunting task, especially when trying 
to visit multiple must-see destinations and national parks along the way. My proposed 
road trip planner will help users create the perfect itinerary for their journey, considering 
factors such as distance, travel time, and points of interest (POI). By integrating 
geospatial data and some routing algorithms, my road trip planner will provide users with 
a comprehensive and optimized route from point A to point B.

## Environment Set-up
Download all the files to your working directory.
```bash
conda env create -n ENVNAME --file environment.yml
```
Replace ENVNAME to your virual environment

## API key
You can sign up OpenRouteService account here https://openrouteservice.org/dev/#/signup. "IT IS FREE!"

Then replace your API Key in planner.py.
```Python
    # Replace 'your_api_key' with your actual OpenRouteService API key
    client = openrouteservice.Client(key='your_api_key')
```
You do not have to have the Google Maps API Key to run the program, unless you want to add more acquire more data.

## Run the project


Activate the environment with following command
```bash
conda activate ENVNAME
```
Replace ENVNAME to your virual environment

Run app.py file.
```bash
Python3 app.py
```
Then click on the URL in Terminal 