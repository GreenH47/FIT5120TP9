import random
import json
from geopy.geocoders import Nominatim

# Create a geocoder instance
geolocator = Nominatim(user_agent="random_locations")

# Generate random Melbourne locations
# List of waste collection bin types
waste_bins = ["General Waste", "Recycling", "Organic", "Compost", "Hazardous", "E-Waste"]
locations = []
i = 0
for i in range(1):
    # Generate random latitude and longitude within the given boundaries
    latitude = random.uniform(-37.9596, -37.7738)
    longitude = random.uniform(144.7776, 145.0488)

    # Reverse geocode the coordinates to get the suburb
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    suburb = location.raw.get('address', {}).get('suburb', '')

    # if the suburb is empty, rengenerate the random latitude and longitude
    while suburb == '':
        latitude = random.uniform(-37.9596, -37.7738)
        longitude = random.uniform(144.7776, 145.0488)
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        suburb = location.raw.get('address', {}).get('suburb', '')

    # generate randome collected_date in week-day-hour-minute format
    collected_date = "week "+ str(random.randint(1, 4)) + " - " + "days: "+str(random.randint(1, 5)) \
                     + " - hours: "+str(random.randint(8, 16)) + ":" + str(random.randint(0, 59))



    # Create a random item from the waste_bins list
    random_bins = random.choice(waste_bins)

    # Create a location object
    location_data = {
        "ID": i,
        "latitude": latitude,
        "longitude": longitude,
        "suburb": suburb,
        "type": random_bins,
        "description": "xx",
        "collected_date": collected_date,
    }

    # Append the location to the list
    locations.append(location_data)

    if i % 10 == 0:
        print("the "+str(i)+ " precentage data has generated")


# Store the locations in a JSON file
with open('random_locations1.json', 'w',encoding="utf-8") as f:
    json.dump(locations, f, indent=4)

