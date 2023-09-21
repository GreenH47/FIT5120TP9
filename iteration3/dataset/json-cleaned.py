import json

cleaned_data = []
uncleaned_data = []

# Load the JSON data from 'casey.json'
with open('casey.json', 'r') as file:
    data = json.load(file)

# Iterate through the data and transform the "geo_shape" field
for item in data:
    geo_shape = item['geo_shape']
    coordinates = []
    try:
        # Split the "geo_shape" string and extract the longitude and latitude values
        for entry in geo_shape.strip('[]').split('], ['):
            if ',' in entry:
                lon, lat = entry.split(', ')
            else:
                lon, lat = entry.split()
            coordinates.append({
                "longitude": float(lon),
                "latitude": float(lat)
            })
        # Replace the "geo_shape" field with the transformed dictionary
        item['geo_shape'] = coordinates
        cleaned_data.append(item)
    except Exception as e:
        uncleaned_data.append(item)
        print(f"Error processing item: {item}")
        print(f"Error message: {str(e)}")

# Save the cleaned data to 'casey-cleaned.json'
with open('casey-cleaned.json', 'w') as file:
    json.dump(cleaned_data, file, indent=4)

# Save the uncleaned data to 'casey-uncleaned.json'
with open('casey-uncleaned.json', 'w') as file:
    json.dump(uncleaned_data, file, indent=4)
