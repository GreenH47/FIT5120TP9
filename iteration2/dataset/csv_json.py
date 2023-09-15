import csv
import json


def convert_csv_to_json(csv_file, json_file):
    # Open the CSV file for reading
    with open(csv_file, 'r',encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Initialize an empty list to store the data records
        data = []

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Convert "longitude" and "latitude" values to float
            row['longtitude'] = float(row['longtitude'])
            row['latitude'] = float(row['latitude'])

            # Append the row as a dictionary to the data list
            data.append(row)

    # Open the JSON file for writing
    with open(json_file, 'w') as file:
        # Write the data list as JSON to the file
        json.dump(data, file, indent=2)


# Example usage
convert_csv_to_json('map_function.csv', 'map_function.json')
